import types
from typing import Any, Optional
from django import http
from django.db import models
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView, TemplateView, RedirectView, FormView

from constants.utils import ConstantsMixin
from django.views.generic.base import View


class CartView(ConstantsMixin, TemplateView):
    template_name = 'ecommerce/index.html'
    #model = ''



    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context_page = {}
        context_page['title'] = 'Каталог'
        context_page['description'] = """
            <p>На этой странице представлен весь ассортимент, предлагаемый компанией. Для вашего удобства мы разделили каталог на категории и подкатегории. Даже неопытный пользователь интернета сможет выбрать для себя нужную мебель для любой зоны офиса.<br />
            Стоимость офисной мебели %city_name_two% доступна, так как мы не делаем большой наценки на товар от производителя. Достигнуть этого удалось благодаря внушительному товарообороту.<br />
            Если вам трудно подобрать мебель самостоятельно, то звоните нам по указанному номеру %phone% или свяжитесь с менеджером по электронной почте: %mail%. Он поможет вам выбрать комплект элементов мебели, чтобы ваш офис выглядел солидно, но при этом в нем было комфортно работать.</p>
        """
        context_page['meta_title'] = 'Каталог мебели интернет-магазина «Офисная мебель АЛЬФА-М» %city_name%'
        context_page['meta_description'] = 'каталог, интернет-магазин, офисная мебель, мебель для персонала, кабинеты для руководителя, офисные кресла, %city_name%'
        context_page['meta_keywords'] = 'Каталог офисной мебели интернет-магазина «Офисная мебель АЛЬФА-М» %city_name%. Качественная мебель для офиса по низкой цене.'
        
        context_constants = self.get_constants()
        
        context = context | context_constants

        return context



class AddToCart(FormView):
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        
        id = int(request.POST['id'])
        qty = None
        url = request.POST['url_from']
        cart = request.session.get('cart')

        try:
            qty = int(request.POST['qty'])
        except:
            return redirect(url)
        print(True)
        if cart:
            request.session['cart'] = list(request.session['cart'])
        else:
            request.session['cart'] = list()

        
        item_exist = None
        for item in request.session['cart']:
            if item['id'] == id:
                item['qty'] = qty
                item_exist = True

        add_data = {
            'id': id,
            'qty': qty,
        }

        if not item_exist:
            request.session['cart'].append(add_data)
            request.session.modified = True

        return redirect(url)
        #return super().post(request, *args, **kwargs)


class RemoveFromCart(View):
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        for item in request.session['cart']:
            if item['type'] == request.POST.get('type') and item['id'] == self.request['id']: #GHJDTHBNM!
                item.clear()

        while {} in request.session['cart']:
            request.session['cart'].remove({})

        if not request.session['cart']:
            del request.session['cart']

        request.session.modified = True
        
        return super().post(request, *args, **kwargs)
    
class DeleteCart(View):
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if request.session.get('cart'):
            del request.session['cart']
        return redirect('/cart/')