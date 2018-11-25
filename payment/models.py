from django.db import models

class Order(models.Model):

    order_id = models.IntegerField()
    terminal_id = models.CharField(max_length=10)
    total_amount = models.IntegerField()