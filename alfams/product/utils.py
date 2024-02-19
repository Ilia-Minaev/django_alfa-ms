from product.models import Categories, Series, Products
from characteristics.models import ProductBrand, ProductClass, ProductFurniture, ProductCountry
from django.urls import reverse_lazy

class ProductMixin():

    obj = None

    def get_category(self, **kwargs):
        if self.obj:
            return self.obj
        else:
            url = self.kwargs['slug']
            self.obj = super().get_queryset().get(slug=url)
            return self.obj
        
    def get_meta_product(self, **kwargs):
        context = kwargs
        page = self.get_category()

        context['title'] = page.title
        context['description'] = page.description
        context['meta_title'] = page.meta_title or page.title
        context['meta_description'] = page.meta_description or page.title
        context['meta_keywords'] = page.meta_keywords or page.title

        return context
    

class BreadcrumbsMixin():
    slug_list = None

    def _get_slugs(self, **kwargs):
        url = self.request.get_full_path()[1:-1]
        slug_list = url.split('/')
        self.slug_list = slug_list

        return slug_list

    def _breadcrumbs_start(self, **kwargs):
        breadcrumbs_list = [
            {
                'title': 'Главная',
                'full_slug': '/',
            },
            {
                'title': 'Каталог',
                'full_slug': reverse_lazy('shop:category'),
            },
        ]
        return breadcrumbs_list

    def _breadcrumbs_category(self, kwargs):
        categories = []
        for item in kwargs:
            try:
                cat = Categories.objects.get(slug=item)
            except:
                raise
            categories.append({
                'title': cat.title,
                'full_slug': cat.get_absolute_url(),
            })

        return categories

    def _breadcrumbs_series(self, kwargs):
        item = Series.objects.get(slug=kwargs)
        return [{
            'title': item.title,
            'full_slug': item.get_absolute_url(),
        }]
    
    def _breadcrumbs_product(self, kwargs):
        item = Products.objects.get(slug=kwargs)
        return [{
            'title': item.title,
            'full_slug': item.get_absolute_url(),
        }]
    

    def breadcrumbs_category(self, **kwargs):
        slug_list = self._get_slugs()

        breadcrumbs_start = self._breadcrumbs_start(kwargs=slug_list)
        breadcrumbs_category = self._breadcrumbs_category(kwargs=slug_list[2:])

        return breadcrumbs_start + breadcrumbs_category

    def breadcrumbs_series(self, **kwargs):
        slug_list = self._get_slugs()

        breadcrumbs_start = self._breadcrumbs_start(kwargs=slug_list)
        breadcrumbs_category = self._breadcrumbs_category(kwargs=slug_list[2:-1])
        breadcrumbs_series = self._breadcrumbs_series(kwargs=slug_list[-1])

        return breadcrumbs_start + breadcrumbs_category + breadcrumbs_series
    
    def breadcrumbs_product(self, **kwargs):
        slug_list = self._get_slugs()
        i = len(slug_list)

        breadcrumbs_start = self._breadcrumbs_start(kwargs=slug_list)
        breadcrumbs_category = self._breadcrumbs_category(kwargs=slug_list[2:i-2])
        breadcrumbs_series = self._breadcrumbs_series(kwargs=slug_list[i-2])
        breadcrumbs_product = self._breadcrumbs_product(kwargs=slug_list[i-1])

        return breadcrumbs_start + breadcrumbs_category + breadcrumbs_series + breadcrumbs_product
    
    def breadcrumbs_test(self, *args, **kwargs):
        parent_list = []
        obj = None
        try:
            obj = super().get_queryset().get(slug=self.kwargs.get('slug'))
            parent_list.append(obj)
        except:
            obj = None

        def _bb(obj):
            if obj.parent:
                parent_list.append(obj.parent)
                _bb(obj.parent)
        if obj:
            _bb(obj)
        

        parent_list.reverse()
        breadcrumbs = self._breadcrumbs_start()
        for item in parent_list:
            breadcrumbs.append(
                {
                    'title': item.title,
                    'full_slug': item.get_absolute_url()
                }
            )

        return breadcrumbs


from django.core.files.storage import FileSystemStorage, default_storage
from django.conf import settings
import time
import pandas as pd
import numpy as np
class Import_Upload():
    file = None
    brand = None
    series = None

    def start_import(self, file):

        folder = settings.MEDIA_ROOT / 'import'
        fs = FileSystemStorage(location=folder)
        file_name = fs.save(file.name, file)
        self.file = file
        file = fs.open(file_name)
        exel = pd.read_excel(
            file,
            #header=None,
            #index_col=0,
            #skiprows=0, 
            usecols='A:AH'
        )

        exel = exel.to_dict('records')
        self.import_upload(exel)
        

    def import_upload(self, exel):
        iteration = {1: True, 2: True}
        for row in exel:
            # Стандартный цвет 	Материал столешницы	Обивка	Подлокотники	Механизм качания	Крестовина	Газпатрон	Ролики	Каркас	Набивка кресла
            props = {}
            props['parent'] = row['Категория']
            props['product_code'] = row['Код товара']
            props['product_article'] = row['Артикул']
            props['product_brand'] = row['Производитель']
            self.brand = props['product_brand']
            props['series'] = row['Серия']
            self.series = props['series']
            props['title'] = row['Наименование']
            props['title_short'] = row['Краткое наименование']
            props['color_material'] = row['Группы цветов']
            props['product_color'] = row['Цвет']
            props['product_country'] = row['Страна-Производитель']
            props['product_price'] = row['Цена']
            #props['product_production_time'] = props['']
            props['product_delivery_time'] = row['Срок поставки']
            props['product_guarantee'] = row['Гарантия']
            props['product_class'] = row['Тип']
            props['product_furniture'] = row['Группа']
            props['description'] = row['Описание']
            props['active'] = row['Актив']
            props['image'] = row['Картинки']
            props['product_height'] = row['Высота']
            props['product_width'] = row['Ширина']
            props['product_length'] = row['Длина']
            props['product_diameter'] = row['Диаметр']
            props['product_weight'] = row['Вес']
            props['product_top_table'] = row['Толшина столешницы']

            if iteration[1]:
                self.series_check(props)
                iteration[1] = False
                continue
            if iteration[2]:
                iteration[2] = False
                continue

    def series_check(self, *args, **kwargs):
        props = args[0]
        #try:
        #    obj = Series.objects.get(product_code=props['product_code'])
        #    args = (props, obj)
        #    self.series_create_update(args)
        #except:
        #    args = (props, Series())
        #    self.series_create_update(*args)

        obj = Series.objects.filter(product_code=props['product_code'])
        if obj.exists():
            obj = obj[0]
            args = (props, obj)
            self.series_create_update(*args)
        else:
            args = (props, Series())
            self.series_create_update(*args)


    def series_create_update(self, *args, **kwargs,):
        props = args[0]
        obj = args[1]

        obj.title = props['title']
        obj.product_article = props['product_article']
        obj.product_code = props['product_code']
        parent = Categories.objects.filter(title=props['parent'])[0]
        obj.parent = parent
        #obj.image = props['image']

        obj.product_call_us = False
        obj.product_recommended = False

        obj.product_price = props['product_price']

        obj.product_guarantee = props['product_guarantee']
        obj.product_top_table = props['product_top_table']
        #product_production_time = props['product_production_time']
        obj.product_delivery_time = props['product_delivery_time']
        
        obj.product_brand = ProductBrand.objects.get(title=self.brand)
        obj.product_class = ProductClass.objects.get(title=props['product_class'])
        #obj.product_furniture = ProductFurniture.objects.get(title=props['product_furniture'])
        #obj.product_color = props['product_color']
        obj.file_import = self.file
        #obj.gallery = None


        obj = obj.save()
        obj_new = Series.objects.filter(title=props['title'])[0]

        from re import split
        countries = split(', |-|,', props['product_country'])
        countries_list = []
        for item in countries:
            country = ProductCountry.objects.get(title=item)
            countries_list.append(country)

        obj_new.product_country.add(*countries_list)
        obj_new.save()

        return True




    def _get_color_code(code):
        return code.split('_')[0]