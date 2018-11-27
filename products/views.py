from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required

@login_required
def list_products(request):
    products_list = Product.objects.all()
    cant_products = Product.objects.count()
    return render(
        request,
        'products/index.html',
        {
            "products_list" : products_list,
            "num" : cant_products
        }
    )