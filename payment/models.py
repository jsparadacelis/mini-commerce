from users.models import Client
from django.db import models

class Order(models.Model):

    terminal_id = models.CharField(max_length=10)
    total_amount = models.FloatField()
    order_token = models.CharField(max_length=20)
    date_order = models.DateField(auto_now=True)
    status = models.CharField(max_length=10)
    token_response = models.CharField(max_length=100)
    user = models.ForeignKey(Client, on_delete=models.CASCADE, default = None)

class Item(models.Model):

    name = models.TextField(max_length = 20)
    value = models.FloatField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)