# Generated by Django 5.0 on 2023-12-22 21:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characteristics', '0003_alter_productcolor_title'),
        ('ecommerce', '0003_alter_course_options_alter_course_parent_series'),
        ('product', '0011_remove_products_product_color_products_product_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='Имя клиента')),
                ('email', models.EmailField(max_length=15, verbose_name='email клиента')),
                ('phone', models.CharField(max_length=15, verbose_name='телефон клиента')),
                ('street', models.CharField(max_length=127, verbose_name='улица клиента')),
                ('city', models.CharField(max_length=15, verbose_name='город клиента')),
                ('payment_method', models.CharField(choices=[('1', 'Безналичный расчет'), ('2', 'Банковской картой'), ('3', 'Яндекс-деньги'), ('4', 'Webmoney')], default='1', max_length=127, verbose_name='Способ оплаты')),
                ('comment', models.TextField(max_length=511, verbose_name='Комментарий клиента')),
                ('order', models.TextField(verbose_name='Имя клиента')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Create date')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('id',),
            },
        ),
        migrations.AlterField(
            model_name='course',
            name='parent_brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='characteristics.productbrand', verbose_name='Производитель'),
        ),
        migrations.AlterField(
            model_name='course',
            name='parent_rate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='ecommerce.currencyrates', verbose_name='Курс валюты'),
        ),
        migrations.AlterField(
            model_name='course',
            name='parent_series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='product.series', verbose_name='Серия'),
        ),
    ]
