
from django.urls import path, include, re_path

from ecommerce.views import CartView, AddToCart, RemoveFromCart, DeleteCart, CartOrder


app_name = 'cart'

urlpatterns = [
    path('', CartView.as_view(), name='cart'),


    path('<int:id>/add/', AddToCart.as_view(), name='cart_add'),
    path('<int:id>/remove/', RemoveFromCart.as_view(), name='cart_remove'),
    path('delete/', DeleteCart.as_view(), name='cart_delete'),
    
    path('order/', CartOrder.as_view(), name='cart_order'),
]
