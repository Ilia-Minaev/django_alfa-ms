import types
from typing import Any, Optional
from django import http
from django.db import models
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView, TemplateView, RedirectView, FormView
from django.views.generic.base import View

from constants.utils import ConstantsMixin
from ecommerce.models import Order
from ecommerce.utils import EcommerceMixin, get_total_price, get_products_by_order, get_table_by_order


class CartView(ConstantsMixin, TemplateView):
    template_name = 'ecommerce/index.html'
    #model = ''

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context_page = {}
        context_page['title'] = 'Корзина'
        context_page['description'] = 'Корзина'
        context_page['meta_title'] = 'Корзина'
        context_page['meta_description'] = 'Корзина'
        context_page['meta_keywords'] = 'Корзина'
        
        context_constants = self.get_constants()

        context = context | context_page | context_constants

        context['breadcrumbs'] = [
            {
                'title': 'Главная',
                'full_slug': '/',
            },
            {
                'title': 'Корзина',
                'full_slug': reverse_lazy('cart:cart'),
            },
        ]

        context['total_price'] = get_total_price(get_products_by_order(self.request.session['cart']))
        
        return context
    
class CartOrder(View):
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        street = request.POST['street']
        city = request.POST['city']
        payment_method = request.POST['payment_method']
        comment = request.POST['comment']
        

        order = get_table_by_order(request.session['cart'])

        order_obj = Order()
        order_obj.name = name
        order_obj.email = email
        order_obj.phone = phone
        order_obj.street = street
        order_obj.city = city
        order_obj.payment_method = payment_method
        order_obj.comment = comment
        order_obj.order = order
        order_obj.order_type = 1
        order_obj.save()


        if request.session.get('cart'):
            del request.session['cart']

        return redirect('/')



class AddToCart(View):
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        
        id = int(request.POST['id'])
        qty = None
        url = request.POST['url_from']
        cart = request.session.get('cart')

        try:
            qty = int(request.POST['qty'])
        except:
            return redirect(url)
        
        if qty < 1:
            return redirect(url)

        if cart:
            request.session['cart'] = list(request.session['cart'])
        else:
            request.session['cart'] = list()
        
        item_exist = None
        for item in request.session['cart']:
            if item['id'] == id:
                item['qty'] = qty
                item_exist = True

        if not item_exist:
            add_data = {
                'id': id,
                'qty': qty,
            }
            request.session['cart'].append(add_data)
            request.session.modified = True

        return redirect(url)
        #return super().post(request, *args, **kwargs)


class RemoveFromCart(View):
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        id = int(request.POST['id'])
        url = request.POST['url_from']
        cart = request.session.get('cart')

        if not cart:
            return redirect(url)

        for item in cart:
            if item['id'] == id:
                item.clear()

        request.session['cart'] = list(filter(None, cart))

        if not cart:
            del request.session['cart']

        request.session.modified = True
        
        return redirect(url)
    
class DeleteCart(View):
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if request.session.get('cart'):
            del request.session['cart']
        return redirect(reverse_lazy('cart:cart'))
    

class FavoritesView(ConstantsMixin, EcommerceMixin, TemplateView):
    template_name = 'ecommerce/favorites.html'
    #model = ''

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context_page = {}
        context_page['title'] = 'Избранное'
        context_page['description'] = 'Избранное'
        context_page['meta_title'] = 'Избранное'
        context_page['meta_description'] = 'Избранное'
        context_page['meta_keywords'] = 'Избранное'
        
        context_constants = self.get_constants()

        context = context | context_page | context_constants

        context['breadcrumbs'] = [
            {
                'title': 'Главная',
                'full_slug': '/',
            },
            {
                'title': 'Избранное',
                'full_slug': reverse_lazy('cart:favorites'),
            },
        ]
        
        context['series'] = self.get_favorites_series()
        context['products'] = self.get_favorites_products()

        return context
    

class FavoritesAddRemove(View):
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        
        id = int(request.POST['id'])
        url = request.POST['url_from']
        model = request.POST['type']
        favorites = request.session.get('favorites')
        item_exist = False

        if favorites:
            favorites = list(favorites)
        else:
            request.session['favorites'] = list()
            favorites = request.session['favorites']
        
        if model == 'series':
            for item in favorites:
                if item.get('id') == id and item.get('type') == model:
                    item.clear()
                    item_exist = True

            if not item_exist:
                add_data = {
                    'id': id,
                    'type': model,
                }
                favorites.append(add_data)
        
        if model == 'product':
            from product.models import Products
            from itertools import chain

            ids = Products.objects.get(pk=id).product_code_color
            ids = Products.objects.filter(product_code_color=ids).values_list('id')
            ids = list(ids)
            ids = list(chain(*ids))

            for item in favorites:
                for item_id in ids:
                    if item.get('id') == item_id and item.get('type') == model:
                        item.clear()
                        item_exist = True
            
            if not item_exist:
                for item_id in ids:
                    add_data = {
                        'id': item_id,
                        'type': model,
                    }
                    favorites.append(add_data)

        request.session['favorites'] = list(filter(None, favorites))
        request.session.modified = True

        return redirect(url)
    

class PrintView(ConstantsMixin, TemplateView):
    template_name = 'ecommerce/print.html'
    #model = ''

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context_page = {}
        context_page['title'] = 'Корзина | Версия для печати'
        context_page['description'] = 'Корзина | Версия для печати'
        context_page['meta_title'] = 'Корзина | Версия для печати'
        context_page['meta_description'] = 'Корзина | Версия для печати'
        context_page['meta_keywords'] = 'Корзина | Версия для печати'
        
        context_constants = self.get_constants()

        context = context | context_page | context_constants

        context['cart'] = self.request.session['cart']

        return context
        

class CallbackOrder(View):
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        
        name = request.POST['name']
        email = '####'
        phone = request.POST['phone']
        street = '####'
        city = '####'
        payment_method = 1
        comment = '####'
        order = '####'

        url = request.POST['url_from']

        order_obj = Order()
        order_obj.name = name
        order_obj.email = email
        order_obj.phone = phone
        order_obj.street = street
        order_obj.city = city
        order_obj.payment_method = payment_method
        order_obj.comment = comment
        order_obj.order = order
        order_obj.order_type = request.POST['order_type']
        order_obj.save()

        return redirect(url)