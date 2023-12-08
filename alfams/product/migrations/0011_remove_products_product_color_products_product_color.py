# Generated by Django 4.2.6 on 2023-12-04 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characteristics', '0003_alter_productcolor_title'),
        ('product', '0010_alter_products_product_code_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='product_color',
        ),
        migrations.AddField(
            model_name='products',
            name='product_color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='product_color', to='characteristics.productcolor', verbose_name='Цвет'),
        ),
    ]
