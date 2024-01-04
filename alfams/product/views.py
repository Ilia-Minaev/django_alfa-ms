import types
from typing import Any, Optional
from django import http
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.db.models.query import QuerySet
from django.db.models import Q
from django.views.generic import ListView, DetailView, TemplateView, RedirectView, FormView

from product.models import Categories, Series, Products
from constants.utils import ConstantsMixin
from product.utils import ProductMixin, BreadcrumbsMixin


class ShopRedirectView(RedirectView):
    url = reverse_lazy('shop:category')

class CategoryView(ConstantsMixin, ProductMixin, BreadcrumbsMixin, ListView):
    model = Categories
    template_name = 'product/index.html'
    context_object_name = 'categories'
    
    def get_queryset(self):
        if not self.kwargs.get('slug'):
            return super().get_queryset().filter(parent=None).filter(is_published=True)
        else:
            category_current = self.get_category()
            categories = super().get_queryset().filter(parent=category_current.pk).filter(is_published=True)
            return categories
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.kwargs.get('slug'):
            context_page = self.get_meta_product()
            context['series'] = Series.objects.filter(parent=self.get_category().pk).filter(is_published=True)
        else:
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
        
        context = context | context_page | context_constants

        context['breadcrumbs'] = self.breadcrumbs_category()
        
        return context
    

class SeriesSingleView(ConstantsMixin, ProductMixin, BreadcrumbsMixin, DetailView):
    model = Series
    template_name = 'product/single_series.html'
    context_object_name = 'series'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        try:
            return super().get(request, *args, **kwargs)
        except:
            url = self.request.get_full_path().replace('series', 'category')
            return redirect(url)

    def get_queryset(self):
        return super().get_queryset() 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_page = self.get_meta_product()
        context_constants = self.get_constants()
        context = context | context_page | context_constants

        context['breadcrumbs'] = self.breadcrumbs_series()

        context['products'] = Products.objects.filter(parent=self.get_category().pk).filter(is_published=True)

        return context
    
class ProductSingleView(ConstantsMixin, ProductMixin, BreadcrumbsMixin, DetailView):
    model = Products
    template_name = 'product/single_product.html'
    context_object_name = 'product'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        try:
            return super().get(request, *args, **kwargs)
        except:
            url = self.request.get_full_path().replace('product', 'series')
            return redirect(url)

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_page = self.get_meta_product()
        context_constants = self.get_constants()
        context = context | context_page | context_constants

        context['products_colors'] = super().get_queryset().filter(product_code_color=self.get_category().product_code_color).filter(is_published=True)

        context['breadcrumbs'] = self.breadcrumbs_product()

        return context
    

class SearchView(ConstantsMixin, ProductMixin, BreadcrumbsMixin, ListView):
    model = Products
    template_name = 'product/search.html'
    #context_object_name = 'product'

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('search')
        query = ' '.join(query.split())

        context = super().get_context_data(**kwargs)

        context_page = {}
        context_page['title'] = 'Поиск по сайту | ' + query
        context_page['description'] = 'Поиск по сайту | ' + query
        context_page['meta_title'] = 'Поиск по сайту | ' + query
        context_page['meta_description'] = 'Поиск по сайту | ' + query
        context_page['meta_keywords'] = 'Поиск по сайту | ' + query

        context_constants = self.get_constants()
        
        context = context | context_page | context_constants

        context['breadcrumbs'] = [
            {
                'title': 'Главная',
                'full_slug': '/',
            },
            {
                'title': 'Поиск',
                'full_slug': reverse_lazy('shop:search'),
            },
        ]

        context['series'] = Series.objects.filter(
            Q(title__contains=query) | Q(product_article__contains=query) | Q(product_code__contains=query)
        ).filter(is_published=True)
        
        context['products'] = Products.objects.filter(
            Q(title__contains=query) | Q(product_article__contains=query) | Q(product_code__contains=query)
        ).filter(is_published=True)

        return context