from django.urls import path

from example.views import index, price


urlpatterns = [
    path('', index),
    path('price', price/),
]
