from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils.safestring import mark_safe
from django.contrib import admin

from datetime import datetime, date

from gallery.models import Name, Images
from characteristics.models import ProductBrand, ProductCountry, ProductClass, ProductFurniture, ProductColor


class ProductBaseModel(models.Model):
    is_published = models.BooleanField(default=True)
    title = models.CharField(max_length=127, blank=False, verbose_name='title')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='url')
    full_slug = models.CharField(max_length=510, verbose_name='full_slug', blank=True)
    description = models.TextField(blank=True, null=True, verbose_name='description')
    meta_title = models.CharField(max_length=127, blank=True, verbose_name='meta_title')
    meta_keywords = models.CharField(max_length=127, blank=True, verbose_name='meta_keywords')
    meta_description = models.TextField(max_length=510, blank=True, verbose_name='meta_description')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Create date')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Update date')

    def show_img(self):
        if self.image:
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100" height="100"></a>'.format(self.image.url))
        else:
            return mark_safe('<div style="color:red">No photo</div>')
        
    show_img.short_description = 'Image'
    show_img.allow_tags = True

    def __str__(self):
        return self.title

    class Meta:
       abstract = True

class Categories(ProductBaseModel):
    image = models.ImageField(upload_to='uploads/category/%Y-%m-%d/', blank=True, verbose_name='image')
    parent = models.ForeignKey('self', blank=True, null=True, related_name='+', verbose_name='parent_category', on_delete=models.PROTECT)
    children = models.ManyToManyField('self', blank=True, related_name='+', verbose_name='children_category', symmetrical=False)
    level = models.PositiveSmallIntegerField(default=0, blank=False)
    icon = models.FileField(upload_to='uploads/category/%Y-%m-%d/', blank=True, verbose_name='icon', help_text='svg or img, 50x50px')

    def show_icon(self):
        if self.icon:
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="20" height="20"></a>'.format(self.icon.url))
        else:
            return mark_safe('<div style="color:red">No photo</div>')
            #return u'<p>No photo</p>'
        
    show_icon.short_description = 'Icon'
    show_icon.allow_tags = True

    def save(self, commit=False, *args, **kwargs):
        """
            ОШИБКА: при редактировании категории, не меняя парента, у родителя удаляется ребенок
            РЕШЕНО!
        """
        #full_slug
        def create_full_slug(self):
            def _get_parent_url(obj):
                if not obj.parent:
                    return obj.slug
                parent_id = obj.parent_id
                parent = Categories.objects.get(pk=parent_id)
                parent_slug = parent.slug
                if parent.parent:
                    _get_parent_url(parent)
                return parent_slug_list.append(parent_slug)
                
            full_slug = []
            full_slug.append(self.slug)
            parent_slug_list = []
            _get_parent_url(self)
            parent_slug_list.reverse()
            full_slug = full_slug + parent_slug_list
            full_slug.reverse()
            full_slug = '/'.join(full_slug)
            return full_slug
        #lvl
        def _check_correct_attach(id):
            parent = self.parent
            childrens = Categories.objects.filter(parent=id)
            for child in childrens:
                if child == parent:
                    raise ValueError("You cannot save parent category inside his childrens categories.") 
                if child.children:
                    _check_correct_attach(child.pk)
                return True
        #lvl
        def _remove_children_from_parent(self):
            try:
                old_parent_id = Categories.objects.get(pk=self.pk).parent_id
                old_parent = Categories.objects.get(pk=old_parent_id)
                old_parent.children.remove(self.pk)
                return old_parent
            except:
                return False
        #lvl
        def _remove_parent_from_childrens(obj=self, level=0):
            try:
                parent = Categories.objects.get(pk=obj.pk)
                childrens = Categories.objects.filter(parent=parent)
                childrens_list = []
                for child in childrens:
                    child.level = level + 1
                    childrens_list.append(child)
                    if child.children:
                        items = _remove_parent_from_childrens(child, level + 1)
                        childrens_list = childrens_list + items
                return childrens_list
            except:
                return False
                #1 если детей нет
                #2 если дети есть
                #3 если детей нет, но они были
        #lvl
        def _save(self, childrens):
            self.full_slug = create_full_slug(self)
            from django.db import transaction
            with transaction.atomic():
                for child in childrens:
                    super(Categories, child).save(*args, **kwargs)
                return super(Categories, self).save(*args, **kwargs)


        if self.parent == self:
            raise ValueError("You cannot specify yourself in the parent category.")
        
        try:
            current_obj = Categories.objects.get(pk=self.pk)
        except:
            ## ВНИМАНИЕ!!! НУЖНЫ ТЕСТЫ С СОХРАНЕНИЕ БЕЗ ПАРЕНТА, И С СОХАРНЕНИЕМ С ДЕТЬМИ
            return super(Categories, self).save(*args, **kwargs)
        
        try:
            parent = self.level
            child = Categories.objects.get(pk=self.parent_id).level
            if child > parent:
                raise ValueError("You cannot specify yourself in the parent category.")
        except:
            pass
        
        if not self.parent:  
            if self.parent_id == current_obj.parent_id:
                #1 не было родителя
                pass
            else:
                #2 был родитель, но его удалил
                _remove_children_from_parent(self)
            childrens = _remove_parent_from_childrens(self, 0)
            self.level = 0
            

            _save(self, childrens)

        if self.parent:
            _check_correct_attach(self.pk)
            
            if self.parent == current_obj.parent:
                #2 родитель не поменялся. не нужно удалять родителей
                childrens = _remove_parent_from_childrens(self, current_obj.level)
            else:
                #1 родитель поменялся. если родитель поменялся, то у старого родителя нужно удалить детей
                _remove_children_from_parent(self)
                new_parent = Categories.objects.get(pk=self.parent_id)
                childrens = _remove_parent_from_childrens(self, new_parent.level + 1)
                new_parent.children.add(self.pk)
                self.level = new_parent.level + 1

            _save(self, childrens)

    
    #def get_absolute_url(self):
    #    kwargs = {
    #        'category_slug_1': self.slug,
    #        #'category_slug_1': self.slug,
    #    }
    #    return reverse('product:category_1', kwargs=kwargs)
    
    def get_absolute_url(self):
        return reverse_lazy('shop:category') + self.full_slug + '/'


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('level', 'parent_id')



class Series(ProductBaseModel):
    parent = models.ForeignKey(Categories, blank=False, null=False, related_name='parent_series', verbose_name='parent_series', on_delete=models.PROTECT)
    image = models.ImageField(upload_to='uploads/series/%Y-%m-%d/', blank=True, verbose_name='image')

    product_call_us = models.BooleanField(default=False, verbose_name='Баннер "Звоните нам"')
    product_recommended = models.BooleanField(default=False, verbose_name='Рекомендуем')

    product_price = models.PositiveSmallIntegerField(default=0, blank=False, verbose_name='Цена')

    product_article = models.CharField(max_length=30, blank=False, unique=True, verbose_name='Артикул (уникальный)', help_text='Обязательное поле')
    product_code = models.CharField(max_length=30, blank=False, unique=True, verbose_name='Код товара (уникальный)', help_text='Обязательное поле')
    product_guarantee = models.CharField(max_length=30, blank=True, unique=True, verbose_name='Гарантия (год)')
    product_top_table = models.CharField(max_length=30, blank=True, unique=True, verbose_name='Толщина столешницы')
    product_production_time = models.CharField(max_length=30, blank=True, unique=True, verbose_name='Время производства')
    product_delivery_time = models.CharField(max_length=30, blank=True, unique=True, verbose_name='Время доставки')
    
    product_brand = models.ForeignKey(ProductBrand, blank=True, null=True, related_name='series_brand', verbose_name='Производитель (бренд)', on_delete=models.PROTECT)
    product_class = models.ForeignKey(ProductClass, blank=True, null=True, related_name='series_class', verbose_name='Класс товара', on_delete=models.PROTECT)
    product_furniture = models.ForeignKey(ProductFurniture, blank=True, null=True, related_name='series_furniture', verbose_name='Тип мебели', on_delete=models.PROTECT)
    
    product_country = models.ManyToManyField(ProductCountry, blank=True, related_name='series_country', verbose_name='Страна-производитель')
    product_color = models.ManyToManyField(ProductColor, blank=True, related_name='series_color', verbose_name='Цвет')

    gallery = models.ForeignKey(Name, blank=True, null=True, related_name='series_gallery', verbose_name='series_gallery', on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse_lazy('shop:series') + self.full_slug + '/'
    
    def get_colors(self):
        products = Products.objects.filter(parent=self.pk)

        colors = set()

        for item in products:
            colors.add(item.product_color)
        
        return colors
    
    def get_card_slider(self):
        if self.gallery:
            card_slider = Images.objects.filter(parent=self.gallery.pk)
        else:
            card_slider = []
        
        if self.image:
            return [self] + list(card_slider)
        else:
            return card_slider

    
    def get_country(self):
        country_all = self.product_country.all()
        if len(country_all) == 1:
            return country_all.values('title')[0]['title']
        country_list = []
        for item in country_all:
            country_list.append(item.title)
        country_list = '-'.join(country_list)
        return country_list
    
    def check_new_banner(self):
        date_now = datetime.now()
        date_created = self.date_created
        date_now = {
            'y': int(date_now.strftime("%Y")),
            'm': int(date_now.strftime("%m")),
            'd': int(date_now.strftime("%d")),
        }
        date_created = {
            'y': int(date_created.strftime("%Y")),
            'm': int(date_created.strftime("%m")),
            'd': int(date_created.strftime("%d")),
        }
        time_passed = (
            date(date_now['y'], date_now['m'], date_now['d'])
            -
            date(date_created['y'], date_created['m'], date_created['d'])
        ).days
        time_needed = 30 * 6

        if time_passed < time_needed:
            return True
        else:
            return False
    def check_session(self, *args):
        return self

    def save(self, *args, **kwargs):
        if self.parent:
            category_slug = Categories.objects.get(pk=self.parent.pk).full_slug
            self.full_slug = category_slug + '/' + self.slug
        return super(Series, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'



class Products(ProductBaseModel):
    parent = models.ForeignKey(Series, blank=False, null=False, related_name='parent_product', verbose_name='parent_product', on_delete=models.PROTECT)
    image = models.ImageField(upload_to='uploads/product/%Y-%m-%d/', blank=True, verbose_name='image')

    product_price = models.PositiveSmallIntegerField(default=0, blank=False, verbose_name='Цена')

    product_article = models.CharField(max_length=30, blank=True, verbose_name='Артикул (уникальный)', help_text='Не обязательное поле, используется как КРАТКОЕ НАИМЕНОВАНИЕ')
    product_code = models.CharField(max_length=30, blank=False, unique=True, verbose_name='Код товара (уникальный)', help_text='Обязательное поле')
    product_code_color = models.CharField(max_length=30, blank=True, verbose_name='Код объединения товара', help_text='Данный код объединяет товар по цвету')
    product_guarantee = models.CharField(max_length=30, blank=True, verbose_name='Гарантия (год)')
    product_top_table = models.CharField(max_length=30, blank=True, verbose_name='Толщина столешницы')
    product_production_time = models.CharField(max_length=30, blank=True, verbose_name='Время производства')
    product_delivery_time = models.CharField(max_length=30, blank=True, verbose_name='Время доставки')
    
    product_brand = models.ForeignKey(ProductBrand, blank=True, null=True, related_name='product_brand', verbose_name='Производитель (бренд)', on_delete=models.PROTECT)
    product_class = models.ForeignKey(ProductClass, blank=True, null=True, related_name='product_class', verbose_name='Класс товара', on_delete=models.PROTECT)
    product_furniture = models.ForeignKey(ProductFurniture, blank=True, null=True, related_name='product_furniture', verbose_name='Тип мебели', on_delete=models.PROTECT)
    
    product_country = models.ManyToManyField(ProductCountry, blank=True, related_name='product_country', verbose_name='Страна-производитель')
    product_color = models.ForeignKey(ProductColor, null=True, related_name='product_color', verbose_name='Цвет', on_delete=models.PROTECT, )
    
    gallery = models.ForeignKey(Name, blank=True, null=True, related_name='product_gallery', verbose_name='series_gallery', on_delete=models.PROTECT, help_text='Только для 3D галерей')

    product_height = models.PositiveSmallIntegerField(default=0, blank=False, verbose_name='Высота, мм')
    product_width = models.PositiveSmallIntegerField(default=0, blank=False, verbose_name='Ширина, мм')
    product_length = models.PositiveSmallIntegerField(default=0, blank=False, verbose_name='Длина, мм')
    product_diameter = models.PositiveSmallIntegerField(default=0, blank=False, verbose_name='Диаметр, мм')
    product_weight = models.PositiveSmallIntegerField(default=0, blank=False, verbose_name='Вес, кг')

    def get_absolute_url(self):
        return reverse_lazy('shop:product') + self.full_slug + '/'
    
    #def get_colors(self):
        #return self.product_color.all()
    
    @admin.display(description="Материал: Цвет")
    def get_product_material_color(self):
        return f'{self.product_color.parent.title}: {self.product_color.title}'
    
    def get_card_slider(self):
        if self.gallery:
            card_slider = Images.objects.filter(parent=self.gallery.pk)
        else:
            card_slider = []
        
        if self.image:
            return [self] + list(card_slider)
        else:
            return card_slider
    
    def get_country(self):
        country_all = self.product_country.all()
        if len(country_all) == 1:
            return country_all.values('title')[0]['title']
        country_list = []
        for item in country_all:
            country_list.append(item.title)
        country_list = '-'.join(country_list)
        return country_list
    
    def get_price(self):
        from ecommerce.utils import get_price as price_mixin
        return price_mixin(obj=self)

    def save(self, *args, **kwargs):
        parent = Series.objects.get(pk=self.parent.pk)
        
        if self.parent:
            self.full_slug = parent.full_slug + '/' + self.slug
        if not self.slug:
            self.slug = self.product_code
        if not self.product_code_color:
            self.product_code_color = self.product_code.split('_')[0]
        if not self.product_guarantee:
            self.product_guarantee = parent.product_guarantee
        if not self.product_brand:
            self.product_brand = parent.product_brand
        if not self.product_class:
            self.product_class = parent.product_class

        return super(Products, self).save(*args, **kwargs)

        #print(self.product_country)
        #if not self.product_country == None:
        #    obj = Products.objects.get(pk=self.pk)
        #    for item in parent.product_country.all():
        #        print(item.pk)
        #        obj.product_country.add(item)
        #    obj.save()
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
