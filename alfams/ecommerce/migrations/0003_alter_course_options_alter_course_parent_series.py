# Generated by Django 5.0 on 2023-12-15 16:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_alter_currencyrates_options_course'),
        ('product', '0011_remove_products_product_color_products_product_color'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('id',), 'verbose_name': 'Курс', 'verbose_name_plural': 'Курсы'},
        ),
        migrations.AlterField(
            model_name='course',
            name='parent_series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='product.series', verbose_name='серия'),
        ),
    ]
