# Generated by Django 4.2.6 on 2023-11-19 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_series_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_article',
            field=models.CharField(blank=True, help_text='Не обязательное поле, используется как КРАТКОЕ НАИМЕНОВАНИЕ', max_length=30, verbose_name='Артикул (уникальный)'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_delivery_time',
            field=models.CharField(blank=True, max_length=30, verbose_name='Время доставки'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_guarantee',
            field=models.CharField(blank=True, max_length=30, verbose_name='Гарантия (год)'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_production_time',
            field=models.CharField(blank=True, max_length=30, verbose_name='Время производства'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_top_table',
            field=models.CharField(blank=True, max_length=30, verbose_name='Толщина столешницы'),
        ),
    ]
