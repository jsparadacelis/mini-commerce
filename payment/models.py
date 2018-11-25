from django.db import models

class Order(models.Model):

    terminal_id = models.CharField(max_length=10)
    total_amount = models.FloatField()
    order_token = models.CharField(max_length=20)
    date_order = models.DateField(auto_now=True)
    items = models.TextField(max_length=300)
    status = models.CharField(max_length=10)