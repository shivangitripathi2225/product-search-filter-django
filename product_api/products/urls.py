from django.urls import path
from .views import get_products, index

urlpatterns = [
    path('', index),
    path('products', get_products),
]