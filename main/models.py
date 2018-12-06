from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):

    name = models.CharField(max_length=50)
    value = models.IntegerField()
    image = models.ImageField(upload_to='media/')

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    terminal = models.CharField(max_length=20)

class Order(models.Model):

    terminal_id = models.CharField(max_length=20)
    total_amount = models.FloatField()
    order_token = models.CharField(max_length=20)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    status = models.CharField(max_length=10)
    token_response = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default = None)
    payment_link = models.CharField(max_length=200)

class Item(models.Model):

    name = models.TextField(max_length = 20)
    value = models.FloatField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)



