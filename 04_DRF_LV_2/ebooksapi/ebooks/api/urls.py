from django.urls import path
# from ebooks.api.views import EbookListCreate
from ebooks.api.views import (EbookListCreateAPIView, EbookDetailAPIView,
                              ReviewCreateAPIView, ReviewDetailAPIView)

urlpatterns = [
    # path("ebooks/",
    # EbookListCreate.as_view(),
    # name="ebook-list"),

    path("ebooks/",
         EbookListCreateAPIView.as_view(),
         name="ebook-list"),

    path("ebooks/<int:pk>/",
         EbookDetailAPIView.as_view(),
         name="ebook-detail"),

    path("ebooks/<int:ebook_pk>/review/",
         ReviewCreateAPIView.as_view(),
         name="review-ebook"),

    path("reviews/<int:pk>/",
         ReviewDetailAPIView.as_view(),
         name="review-detail")
]
