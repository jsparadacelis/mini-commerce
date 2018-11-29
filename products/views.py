#Django utilities
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#Local files utilities
from .models import Product

@login_required
def list_products(request):

    #Query for all products
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