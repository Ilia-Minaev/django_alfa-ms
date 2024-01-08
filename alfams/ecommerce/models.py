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

class Order(models.Model):
    PAYMENT_VALUES = [
        ('1', 'Безналичный расчет'),
        ('2', 'Банковской картой'),
        ('3', 'Яндекс-деньги'),
        ('4', 'Webmoney'),
    ]
    ORDER_VALUES = [
        ('1', 'Заказ из корзины'),
        ('2', 'Купить в 1 клик'),
        ('3', 'Обратный звонок'),
        ('4', 'Консультация'),
    ]

    name = models.CharField(max_length=127, blank=False, verbose_name='Имя клиента')
    email = models.EmailField(max_length=47, blank=False, verbose_name='email клиента')
    phone = models.CharField(max_length=15, blank=False, verbose_name='телефон клиента')
    street = models.CharField(max_length=127, blank=False, verbose_name='улица клиента')
    city = models.CharField(max_length=47, blank=False, verbose_name='город клиента')
    payment_method = models.CharField(max_length=127, blank=False, choices=PAYMENT_VALUES, default=PAYMENT_VALUES[0][0], verbose_name='Способ оплаты')
    comment = models.TextField(max_length=511, blank=False, verbose_name='Комментарий клиента')
    order = models.TextField(blank=False, verbose_name='Заказ')
    order_type = models.CharField(max_length=127, blank=False, choices=ORDER_VALUES, default=ORDER_VALUES[0][0], verbose_name='Тип заказа')
    
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Create date')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Update date')

    def __str__(self):
        return f'{self.pk} - {self.name}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-id',)