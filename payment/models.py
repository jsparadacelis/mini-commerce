from django.db import models

class Order(models.Model):

    terminal_id = models.CharField(max_length=10)
    total_amount = models.IntegerField()
    date_order = models.DateField(auto_now=True)