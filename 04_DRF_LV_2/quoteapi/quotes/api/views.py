from rest_framework import generics

from quotes.models import Quote
from quotes.api.serializers import QuoteSerializer
from quotes.api.permissions import isAdminUserOrReadOnly

class QuoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Quote.objects.all().order_by("-id")
    serializer_class = QuoteSerializer
    permission_classes = [isAdminUserOrReadOnly]

class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [isAdminUserOrReadOnly]
