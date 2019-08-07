from django.db import models


class Consumable(models.Model):
    name = models.CharField(max_length=30)
    weight = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    description = models.CharField(max_length=100)
