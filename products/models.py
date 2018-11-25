from django.db import models
from payment.models import Order

class Product(models.Model):

    name = models.CharField(max_length=50)
    value = models.IntegerField()
    image = models.ImageField(upload_to='media/')

class Item(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cant = models.IntegerField()
    total_amount = models.IntegerField()
