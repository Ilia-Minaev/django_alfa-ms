
from django.urls import path, include, re_path

from ecommerce.views import CartView


app_name = 'cart'

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    

]
