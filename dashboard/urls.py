from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BaseTemplateView.as_view(), name='index')
]