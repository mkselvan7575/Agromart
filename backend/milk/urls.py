from django.urls import path
from .views import *

urlpatterns = [
    path('api/orders/', OrderCreateView.as_view(), name='order-create'),
    path('api/product/',ProductList.as_view(),name='my products')
]
