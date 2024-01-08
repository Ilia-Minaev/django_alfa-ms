
from django.urls import path, include, re_path

from ecommerce.views import (
    CartView, AddToCart, RemoveFromCart, DeleteCart, CartOrder, PrintView,
    FavoritesView, FavoritesAddRemove,
    CallbackOrder)


app_name = 'cart'

urlpatterns = [
    path('', CartView.as_view(), name='cart'),


    path('<int:id>/add/', AddToCart.as_view(), name='cart_add'),
    path('<int:id>/remove/', RemoveFromCart.as_view(), name='cart_remove'),
    path('delete/', DeleteCart.as_view(), name='cart_delete'),
    path('order/', CartOrder.as_view(), name='cart_order'),
    path('print/', PrintView.as_view(), name='cart_print'),

    path('callback/', CallbackOrder.as_view(), name='callback_order'),

    path('favorites/', FavoritesView.as_view(), name='favorites'),
    path('favorites/<int:id>/action/', FavoritesAddRemove.as_view(), name='favorites_action'),
]
