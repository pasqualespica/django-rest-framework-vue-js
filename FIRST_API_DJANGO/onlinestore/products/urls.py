
from django.urls import path

from products.views import ProductDetailView, ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name="product-list"),
    path('products/<int:pk>/', ProductDetailView.as_view(), name="product-list"),

]

from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

