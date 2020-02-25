# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView
from django.http import JsonResponse
from products.models import Product, Manufacturer

# function base view ...

def product_list(request):
    products = Product.objects.all() # o una porzione [:30]
    # data = {"products" : list(products.values("pk", "name"))}
    data = {"products" : list(products.values())}
    response = JsonResponse(data)
    return response

def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {"product" : {
            "name": product.name,
            "manufacturer" : product.manufacturer.name,
            "description" : product.description,
            "photo" : product.photo.url,
            "price" : product.price,
            "shipping-cost" : product.shipping_cost,
            "quantity" : product.quantity,
        }}
        resposne = JsonResponse(data)
    except Product.DoesNotExist:
        resposne = JsonResponse({
            "error" : { 
                "code" : 404,
                "message" : "prodotto non trovato"
                }},
                status=404) 

    return resposne

# modifiche per prova pratica

def manufacturer_list(request):
    manufacturers = Manufacturer.objects.all() # o una porzione [:30]
    data = {"manufacturers" : list(manufacturers.values())}
    response = JsonResponse(data)
    return response


def manufacturer_detail(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)

        # vogliamo anche i prodotti di un produttore 
        #  vedi `related_name` di Product 
        manufacturer_products = manufacturer.products.all()

        data = {"manufacturer" : {
            "name": manufacturer.name,
            "location": manufacturer.location,
            "active": manufacturer.active,
            "products" : list(manufacturer_products.values())
        }}
        resposne = JsonResponse(data)

    except manufacturer.DoesNotExist:
        resposne = JsonResponse({
            "error" : { 
                "code" : 404,
                "message" : "produttore non trovato"
                }},
                status=404) 

    return resposne

# class ProductDetailView(DetailView):
#     model = Product
#     template_name = "products/product_detail.html"

# class ProductListView(ListView):
#     model = Product
#     template_name = "products/product_list.html"
