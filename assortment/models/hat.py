from django.db import models
from accounting.models.consumable import Consumable

STATUS = [
    (0, 'In Stock'),
    (1, 'Out of Stock'),
]


class Color(models.Model):
    name = models.CharField(max_length=30, unique=True)
    color_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Hat(models.Model):
    name = models.CharField(max_length=100)
    colors = models.ManyToManyField(Color, related_name='hats', through='Availability', blank=True)
    consumables = models.ManyToManyField(Consumable, related_name='hats')
    availability_status = models.IntegerField(choices=STATUS, default=0)
    photo = models.ImageField(blank=True)
    description = models.URLField(max_length=128, unique=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    expense = models.DecimalField(max_digits=5, decimal_places=2)
    revenue = models.DecimalField(max_digits=5, decimal_places=2)
    actual_discount = models.IntegerField(null=True, blank=True)
    spent_time = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.name


class Availability(models.Model):
    state = models.IntegerField(choices=STATUS, default=0)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='availability_options')
    hat = models.ForeignKey(Hat, on_delete=models.CASCADE)
