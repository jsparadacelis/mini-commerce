from django.contrib import admin

from .models import Order, Item, Client, Product

admin.site.register(Order)
admin.site.register(Item)
admin.site.register(Client)
admin.site.register(Product)