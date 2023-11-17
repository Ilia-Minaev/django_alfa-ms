from typing import Any, Optional
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render

from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView, TemplateView

from product.models import Categories, Series, Products
from constants.utils import ConstantsMixin
from product.utils import ProductMixin


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
        context['description'] = """
            <p>На этой странице представлен весь ассортимент, предлагаемый компанией. Для вашего удобства мы разделили каталог на категории и подкатегории. Даже неопытный пользователь интернета сможет выбрать для себя нужную мебель для любой зоны офиса.<br />
            Стоимость офисной мебели %city_name_two% доступна, так как мы не делаем большой наценки на товар от производителя. Достигнуть этого удалось благодаря внушительному товарообороту.<br />
            Если вам трудно подобрать мебель самостоятельно, то звоните нам по указанному номеру %phone% или свяжитесь с менеджером по электронной почте: %mail%. Он поможет вам выбрать комплект элементов мебели, чтобы ваш офис выглядел солидно, но при этом в нем было комфортно работать.</p>
        """
        context['meta_title'] = 'Каталог мебели интернет-магазина «Офисная мебель АЛЬФА-М» %city_name%'
        context['meta_description'] = 'каталог, интернет-магазин, офисная мебель, мебель для персонала, кабинеты для руководителя, офисные кресла, %city_name%'
        context['meta_keywords'] = 'Каталог офисной мебели интернет-магазина «Офисная мебель АЛЬФА-М» %city_name%. Качественная мебель для офиса по низкой цене.'

        context['breadcrumbs'] = self.get_breadcrumbs_cat()
        
        return context
    

class SubCategoryView(ConstantsMixin, ProductMixin, ListView):
    model = Categories
    template_name = 'product/index.html'
    context_object_name = 'categories'

    #def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
    #    category_current = self.get_category()
    #    category_current_full_slug = '/category/' + category_current.full_slug + '/'
    #    url = request.get_full_path()
    #    if url != category_current_full_slug:
    #        raise Http404('Bad url')
    #    return super().get(request, *args, **kwargs)

    def get_queryset(self):
        category_current = self.get_category()
        category_current_full_slug = '/category/' + category_current.full_slug + '/'
        url = self.request.get_full_path()
        if url != category_current_full_slug:
            raise Http404('Bad url')
        
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
    template_name = 'product/single_serie.html'
    context_object_name = 'serie'

    def get_queryset(self):
        #return Series.objects.get(slug='riva')
        return super().get_queryset()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_page = self.get_meta_product()
        context_constants = self.get_constants()
        context = context | context_page | context_constants

        context['breadcrumbs'] = self.get_breadcrumbs_ser()

        #context['series'] = Series.objects.filter(parent=self.get_category().pk).filter(is_published=True)

        return context