from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.exceptions import ValidationError

from ebooks.models import Ebook, Review
from ebooks.api.serializers import EbookSerializer, ReviewSerializer
from ebooks.api.permissions import IsAdminUserOrReadOnly,isReviewAuthorOrReadOnly
from ebooks.api.pagination import SmallSetPagination

class EbookListCreateAPIView(generics.ListCreateAPIView):
    # TO REMOVE following Warning add ORDER_BY
    # UnorderedObjectListWarning: Pagination may yield inconsistent results 
    # with an unordered object_list: < class 'ebooks.models.Ebook' > QuerySet.

    # con il '-' si invert l'ordine ..
    queryset = Ebook.objects.all().order_by("-id")
    serializer_class = EbookSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallSetPagination

class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [IsAdminUserOrReadOnly]

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # sovrascrive il metodo della classe CreateModelMixin
    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        review_author = self.request.user

        review_queryset = Review.objects.filter(ebook=ebook,
                                                review_author=review_author)

        if review_queryset.exists():
            raise ValidationError("Hai gia' recensito questo ebook")

        serializer.save(ebook=ebook, review_author=review_author)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [isReviewAuthorOrReadOnly]

# class EbookListCreate(mixins.ListModelMixin,
#                 mixins.CreateModelMixin,
#                 generics.GenericAPIView):
    
#     queryset = Ebook.objects.all()
#     serializer_class = EbookSerializer

#     def get(self, request, *arg, **kwargs):
#         # a questo punto possiamo ultizzare i metodi che le classi mixins ci
#         # mettono a disposizione
#         return self.list(request, *arg, **kwargs)
    
#     def post(self, request, *arg, **kwargs):
#         # a questo punto possiamo ultizzare i metodi che le classi mixins ci
#         # mettono a disposizione
#         return self.create(request, *arg, **kwargs)
    
