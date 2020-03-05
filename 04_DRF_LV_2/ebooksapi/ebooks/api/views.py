from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework import generics

from ebooks.models import Ebook, Review
from ebooks.api.serializers import EbookSerializer, ReviewSerializer


class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer


class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # sovrascrive il metodo della classe CreateModelMixin
    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        serializer.save(ebook=ebook)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
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
    
