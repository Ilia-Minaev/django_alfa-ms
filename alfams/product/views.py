import types
from typing import Any, Optional
from django import http
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView, TemplateView, RedirectView, FormView

from product.models import Categories, Series, Products
from constants.utils import ConstantsMixin
from product.utils import ProductMixin, BreadcrumbsMixin

"""
class CategoryView(ConstantsMixin, ProductMixin, ListView):
    model = Categories
    template_name = 'product/index.html'
    context_object_name = 'categories'
    
    def get_queryset(self):
        return super().get_queryset().filter(parent=None).filter(is_published=True)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context_page = self.get_page_context()
        context_constants = self.get_constants()
        context = context | context_constants

        context['title'] = 'Каталог'
        context['description'] = "
            <p>На этой странице представлен весь ассортимент, предлагаемый компанией. Для вашего удобства мы разделили каталог на категории и подкатегории. Даже неопытный пользователь интернета сможет выбрать для себя нужную мебель для любой зоны офиса.<br />
            Стоимость офисной мебели %city_name_two% доступна, так как мы не делаем большой наценки на товар от производителя. Достигнуть этого удалось благодаря внушительному товарообороту.<br />
            Если вам трудно подобрать мебель самостоятельно, то звоните нам по указанному номеру %phone% или свяжитесь с менеджером по электронной почте: %mail%. Он поможет вам выбрать комплект элементов мебели, чтобы ваш офис выглядел солидно, но при этом в нем было комфортно работать.</p>
        "
        context['meta_title'] = 'Каталог мебели интернет-магазина «Офисная мебель АЛЬФА-М» %city_name%'
        context['meta_description'] = 'каталог, интернет-магазин, офисная мебель, мебель для персонала, кабинеты для руководителя, офисные кресла, %city_name%'
        context['meta_keywords'] = 'Каталог офисной мебели интернет-магазина «Офисная мебель АЛЬФА-М» %city_name%. Качественная мебель для офиса по низкой цене.'

        context['breadcrumbs'] = self.get_breadcrumbs_cat()
        
        return context
    

class SubCategoryView(ConstantsMixin, ProductMixin, ListView):
    model = Categories
    template_name = 'product/index.html'
    context_object_name = 'categories'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        category_current_full_slug = '/category/' + self.get_category().full_slug + '/'
        url = request.get_full_path()
        if url != category_current_full_slug:
            raise Http404('Bad url')
        
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        category_current = self.get_category()
        categories = Categories.objects.filter(parent=category_current.pk)

        return categories
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_page = self.get_meta_product()
        context_constants = self.get_constants()
        context = context | context_page | context_constants
        
        context['breadcrumbs'] = self.get_breadcrumbs_cat()

        context['series'] = Series.objects.filter(parent=self.get_category().pk).filter(is_published=True)

        return context


class SingleSeries(ConstantsMixin, ProductMixin, DetailView): #DetailView
    model = Series
    template_name = 'product/single_series.html'
    context_object_name = 'series'

    def get_queryset(self):
        return super().get_queryset()
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_page = self.get_meta_product()
        context_constants = self.get_constants()
        context = context | context_page | context_constants

        context['breadcrumbs'] = self.get_breadcrumbs_ser()

        context['products'] = Products.objects.filter(parent=self.get_category().pk)

        return context
"""

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
            categories = super().get_queryset().filter(parent=category_current.pk)
            return categories
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context_page = self.get_page_context()
        if self.kwargs.get('slug'):
            context_page = self.get_meta_product()
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
        if self.kwargs.get('slug'):
            context['series'] = Series.objects.filter(parent=self.get_category().pk).filter(is_published=True)
        
        return context
    

class SeriesSingleView(ConstantsMixin, ProductMixin, BreadcrumbsMixin, DetailView):
    model = Series
    template_name = 'product/single_series.html'
    context_object_name = 'series'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        try:
            return super().get(request, *args, **kwargs)
        except:
            url = self.request.get_full_path().replace('series', 'category').replace(self.kwargs['slug'] + '/', '')
            return redirect(url)


    def get_queryset(self):
        return super().get_queryset()
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_page = self.get_meta_product()
        context_constants = self.get_constants()
        context = context | context_page | context_constants

        context['breadcrumbs'] = self.breadcrumbs_series()

        context['products'] = Products.objects.filter(parent=self.get_category().pk)

        return context
    
class ProductSingleView(ConstantsMixin, ProductMixin, BreadcrumbsMixin, DetailView):
    model = Products
    template_name = 'product/single_product.html'
    context_object_name = 'product'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        try:
            return super().get(request, *args, **kwargs)
        except:
            url = self.request.get_full_path().replace('product', 'series').replace(self.kwargs['slug'] + '/', '')
            return redirect(url)

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_page = self.get_meta_product()
        context_constants = self.get_constants()
        context = context | context_page | context_constants

        context['products_colors'] = super().get_queryset().filter(product_code_color=self.get_category().product_code_color)


        context['breadcrumbs'] = self.breadcrumbs_product()

        return context