from django.contrib import admin
from .models.hat import Hat, Color, Availability

admin.site.register(Hat)
admin.site.register(Color)
admin.site.register(Availability)
