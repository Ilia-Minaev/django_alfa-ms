from product.models import Categories, Series, Products
from characteristics.models import ProductBrand, ProductClass, ProductFurniture, ProductCountry, ProductColor
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
            usecols='A:AG'
        )

        exel = exel.to_dict('records')
        self.import_upload(exel)
        

    def import_upload(self, exel):
        def _check_row(row):
            return False if pd.isna(row) else row
        iteration = {1: True, 2: True}
        for row in exel:
            # Стандартный цвет 	Материал столешницы	Обивка	Подлокотники	Механизм качания	Крестовина	Газпатрон	Ролики	Каркас	Набивка кресла
            props = {}
            props['parent'] = _check_row(row['Категория'])
            props['product_code'] = _check_row(row['Код товара'])
            props['product_article'] = _check_row(row['Артикул'])
            props['product_brand'] = _check_row(row['Производитель'])
            #props['series'] = _check_row(row['Серия'])  #поле удалено
            props['title'] = _check_row(row['Наименование'])
            props['title_short'] = _check_row(row['Краткое наименование'])
            props['color_material'] =_check_row((row['Группы цветов']))
            props['product_color'] = _check_row(row['Цвет'])
            props['product_country'] = _check_row(row['Страна-Производитель'])
            props['product_price'] = _check_row(row['Цена'])
            #props['product_production_time'] = _check_row(props[''])
            props['product_delivery_time'] = _check_row(row['Срок поставки'])
            props['product_guarantee'] = _check_row(row['Гарантия'])
            props['product_class'] = _check_row(row['Тип'])
            props['product_furniture'] = _check_row(row['Группа'])
            props['description'] = _check_row(row['Описание'])
            props['active'] = _check_row(row['Актив'])
            props['image'] = _check_row(row['Картинки'])
            props['product_height'] = _check_row(row['Высота'])
            props['product_width'] = _check_row(row['Ширина'])
            props['product_length'] = _check_row(row['Длина'])
            props['product_diameter'] = _check_row(row['Диаметр'])
            props['product_weight'] = _check_row(row['Вес'])
            props['product_top_table'] = _check_row(row['Толшина столешницы'])

            if iteration[1]:
                self.series_check(props)
                iteration[1] = False
                continue
            elif iteration[2]:
                iteration[2] = False
                continue
            else:
                self.products_check(props)
            

    def series_check(self, *args, **kwargs):
        props = args[0]

        obj = Series.objects.filter(product_code=props['product_code'])
        if obj.exists():
            self.series_create_update(props, obj[0])
        else:
            self.series_create_update(props, Series())


    def series_create_update(self, *args, **kwargs,):
        props = args[0]
        obj = args[1]

        obj.title = props['title'] if props['title'] else ''
        obj.product_article = props['product_article'] if props['product_article'] else ''
        obj.product_code = props['product_code'] if props['product_code'] else ''
        if props['parent']:
            parent = Categories.objects.filter(title=props['parent'])
            if parent.exists(): obj.parent = parent[0]
        #obj.image = props['image'] if props['title'] else ''
        obj.product_call_us = False
        obj.product_recommended = False
        obj.product_price = props['product_price'] if props['product_price'] else ''
        obj.product_guarantee = props['product_guarantee'] if props['product_guarantee'] else ''
        obj.product_top_table = props['product_top_table'] if props['product_top_table'] else ''
        #obj.product_production_time = props['product_production_time'] if props['product_production_time'] else ''
        obj.product_delivery_time = props['product_delivery_time'] if props['product_delivery_time'] else ''
        #obj.product_brand = self.brand
        if props['product_class']:
            obj.product_class = ProductClass.objects.get(title=props['product_class'])
        if props['product_furniture']:
            obj.product_furniture = ProductFurniture.objects.get(title=props['product_furniture'])
        #obj.product_color = props['product_color'] if props['product_color'] else ''
        obj.file_import = self.file
        #obj.gallery = None

        obj.save()
        self.series = obj
        print(self.series)
        self.brand = ProductBrand.objects.get(title=props['product_brand'])
        obj.product_brand = self.brand

        from re import split
        countries = split(', |-|,', props['product_country'])
        countries_list = []
        for item in countries:
            country = ProductCountry.objects.get(title=item)
            countries_list.append(country)

        obj.product_country.add(*countries_list)
        obj.save()

        return True
    

    def products_check(self, *args, **kwargs):
        props = args[0]

        obj = Products.objects.filter(product_code=props['product_code'])
        if obj.exists():
            obj = obj[0]
            args = (props, obj)
            self.products_create_update(*args)
        else:
            args = (props, Products())
            self.products_create_update(*args)


    def products_create_update(self, *args, **kwargs,):
        props = args[0]
        obj = args[1]

        obj.title = props['title']
        obj.product_article = props['product_article']
        obj.product_code = props['product_code']
        #parent = Categories.objects.filter(title=props['parent'])[0]
        
        #obj.image = props['image']

        obj.product_call_us = False
        obj.product_recommended = False

        obj.product_price = props['product_price']

        obj.product_guarantee = props['product_guarantee']
        obj.product_top_table = props['product_top_table']
        #product_production_time = props['product_production_time']
        obj.product_delivery_time = props['product_delivery_time']
        obj.parent = self.series
        obj.product_brand = self.brand
        obj.product_class = ProductClass.objects.get(title=props['product_class'])
        obj.product_furniture = ProductFurniture.objects.get(title=props['product_furniture'])
        obj.product_color = ProductColor.objects.get(title=props['product_color'])
        #obj.product_color = self._get_color_code(props['product_color'])
        #obj.file_import = self.file
        #obj.gallery = None


        obj.save()
        #obj_new = Series.objects.filter(title=props['title'])[0]

        from re import split
        countries = split(', |-|,', props['product_country'])
        countries_list = []
        for item in countries:
            country = ProductCountry.objects.get(title=item)
            countries_list.append(country)

        obj.product_country.add(*countries_list)
        obj.save()

        return True


    def _get_color_code(code):
        return code.split('_')[0]