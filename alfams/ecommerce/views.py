import types
from typing import Any, Optional
from django import http
from django.db import models
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView, TemplateView, RedirectView

from constants.utils import ConstantsMixin


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
