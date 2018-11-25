from django.db import models
from payment.models import Order

class Product(models.Model):

    name = models.CharField(max_length=50)
    value = models.IntegerField()
    image = models.ImageField(upload_to='media/')
