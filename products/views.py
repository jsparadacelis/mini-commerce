from django.shortcuts import render
from .models import Product

# Create your views here.
def list_products(request):
    products_list = Product.objects.all()
    return render(
        request,
        'products/index.html',
        {
            "products_list" : products_list
        }
    )