# Generated by Django 4.2.6 on 2023-11-05 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True, verbose_name='Производитель (бренд)')),
            ],
        ),
        migrations.CreateModel(
            name='ProductClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True, verbose_name='Класс товара')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCountry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='uploads/characteristics/%Y-%m-%d/', verbose_name='image')),
                ('title', models.CharField(max_length=30, unique=True, verbose_name='Страна-производитель')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductFurniture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True, verbose_name='Тип мебели')),
            ],
        ),
        migrations.CreateModel(
            name='ProductMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True, verbose_name='Материал (тип цвета)')),
            ],
        ),
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='uploads/characteristics/%Y-%m-%d/', verbose_name='image')),
                ('title', models.CharField(max_length=30, unique=True, verbose_name='Цвет')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='color_material_parent', to='characteristics.productmaterial', verbose_name='Материал (тип цвета)')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]