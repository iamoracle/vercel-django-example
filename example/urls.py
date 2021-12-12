from django.urls import path

from example.views import index, price, transactions


urlpatterns = [
    path('', index),
    path('price/', price),
    path('transactions/', transactions),
]
