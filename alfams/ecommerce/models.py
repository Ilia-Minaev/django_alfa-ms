from collections.abc import Iterable
from django.db import models
from characteristics.models import ProductBrand
from product.models import Series


class CurrencyRates(models.Model):
    title = models.CharField(max_length=127, blank=False, verbose_name='title')
    rate = models.PositiveSmallIntegerField(verbose_name='Курс валюты, %')

    def save(self, *args, **kwargs):
        if not self.rate:
            self.rate = 0
        return super(CurrencyRates, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс валюты'
        verbose_name_plural = 'Курсы валют'
        ordering = ('id',)


class Course(models.Model):
    parent_series = models.ForeignKey(Series, blank=False, null=False, related_name='+', verbose_name='Серия', on_delete=models.PROTECT)
    parent_brand = models.ForeignKey(ProductBrand, blank=False, null=False, related_name='+', verbose_name='Производитель', on_delete=models.PROTECT)
    parent_rate = models.ForeignKey(CurrencyRates, blank=False, null=False, related_name='+', verbose_name='Курс валюты', on_delete=models.PROTECT)
    extra_charge = models.PositiveSmallIntegerField(verbose_name='Наша наценка, %')
    discount_real = models.PositiveSmallIntegerField(verbose_name='Скидка производителя, %')
    discount_fake = models.PositiveSmallIntegerField(verbose_name='Фейковая скидка, %')

    def __str__(self):
        return f'{self.parent_brand} - {self.parent_series}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ('id',)

