from collections.abc import Iterable
from django.db import models
from django.utils.safestring import mark_safe


class CharacteristicsBaseModel(models.Model):
    image = models.ImageField(upload_to='uploads/characteristics/%Y-%m-%d/', blank=True, verbose_name='image')
    def show_img(self):
        if self.image:
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="" height="100"></a>'.format(self.image.url))
        else:
            return mark_safe('<div style="color:red">No photo</div>')
        
    show_img.short_description = 'Image'
    show_img.allow_tags = True

    class Meta:
       abstract = True


class ProductBrand(CharacteristicsBaseModel):
    title = models.CharField(max_length=30, blank=False, unique=True, verbose_name='Производитель (бренд)')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.title = self.title.lower()
        return super(ProductBrand, self).save(*args, **kwargs)
    
class ProductCountry(CharacteristicsBaseModel):
    title = models.CharField(max_length=30, blank=False, unique=True, verbose_name='Страна-производитель')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.title = self.title.lower()
        return super(ProductCountry, self).save(*args, **kwargs)

class ProductClass(models.Model):
    title = models.CharField(max_length=30, blank=False, unique=True, verbose_name='Класс товара')\
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.title = self.title.lower()
        return super(ProductClass, self).save(*args, **kwargs)
    
class ProductFurniture(models.Model):
    title = models.CharField(max_length=30, blank=False, unique=True, verbose_name='Тип мебели')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.title = self.title.lower()
        return super(ProductFurniture, self).save(*args, **kwargs)

class ProductMaterial(models.Model):
    title = models.CharField(max_length=30, blank=False, unique=True, verbose_name='Материал (тип цвета)')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.title = self.title.lower()
        return super(ProductMaterial, self).save(*args, **kwargs)
    
class ProductColor(CharacteristicsBaseModel):
    title = models.CharField(max_length=30, blank=False, verbose_name='Цвет')
    parent = models.ForeignKey(ProductMaterial, blank=True, null=True, related_name='color_material_parent', verbose_name='Материал (тип цвета)', on_delete=models.PROTECT)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.title = self.title.lower()
        return super(ProductColor, self).save(*args, **kwargs)