from django.urls import path
from .views import create_item, list_item, invoice,calculate_discount

urlpatterns = [
    path('', create_item, name='create_item'),
    path('list/', list_item, name='list_item'),
    path('invoice/', invoice, name='invoice'),
    # path('invoice/', invoice, name='invoice'),
    path('calculate_discount/', calculate_discount, name='calculate_discount'),
]
