
from django.urls import path

# from products.views import ProductDetailView, ProductListView
from products.views import (product_list, product_detail,
                            manufacturer_detail, manufacturer_list ) 

urlpatterns = [
    # ora invece specifichiamo il nostro ENDPOINT
    path('products/', product_list, name="product-list"),
    path('products/<int:pk>/', product_detail, name="product-detail"),

    path('manufacturers/', manufacturer_list, name="manufacturer-list"),
    path('manufacturers/<int:pk>/', manufacturer_detail, name="manufacturer-detail"),

    # path('', ProductListView.as_view(), name="product-list"),
    # path('products/<int:pk>/', ProductDetailView.as_view(), name="product-detail"),

]

# from django.conf.urls.static import static
# from django.conf import settings

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

