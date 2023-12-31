# Generated by Django 4.2.6 on 2023-11-05 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_alter_images_options_alter_name_options'),
        ('characteristics', '0001_initial'),
        ('product', '0005_categories_full_slug_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=127, verbose_name='title')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='url')),
                ('full_slug', models.CharField(blank=True, max_length=510, verbose_name='full_slug')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('meta_title', models.CharField(blank=True, max_length=127, verbose_name='meta_title')),
                ('meta_keywords', models.CharField(blank=True, max_length=127, verbose_name='meta_keywords')),
                ('meta_description', models.TextField(blank=True, max_length=510, verbose_name='meta_description')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Create date')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('image', models.ImageField(blank=True, upload_to='uploads/series/%Y-%m-%d/', verbose_name='image')),
                ('product_call_us', models.BooleanField(default=False, verbose_name='Баннер "Звоните нам"')),
                ('product_recommended', models.BooleanField(default=False, verbose_name='Рекомендуем')),
                ('product_price', models.PositiveSmallIntegerField(default=0, verbose_name='Цена')),
                ('product_article', models.CharField(help_text='Обязательное поле', max_length=30, unique=True, verbose_name='Артикул (уникальный)')),
                ('product_code', models.CharField(help_text='Обязательное поле', max_length=30, unique=True, verbose_name='Код товара (уникальный)')),
                ('product_guarantee', models.CharField(blank=True, max_length=30, unique=True, verbose_name='Гарантия (год)')),
                ('product_top_table', models.CharField(blank=True, max_length=30, unique=True, verbose_name='Толщина столешницы')),
                ('product_production_time', models.CharField(blank=True, max_length=30, unique=True, verbose_name='Время производства')),
                ('product_delivery_time', models.CharField(blank=True, max_length=30, unique=True, verbose_name='Время доставки')),
                ('gallery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='series_gallery', to='gallery.name', verbose_name='series_gallery')),
                ('product_brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='series_brand', to='characteristics.productbrand', verbose_name='Производитель (бренд)')),
                ('product_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='series_class', to='characteristics.productclass', verbose_name='Класс товара')),
                ('product_color', models.ManyToManyField(blank=True, related_name='series_color', to='characteristics.productcolor', verbose_name='Цвет')),
                ('product_country', models.ManyToManyField(blank=True, related_name='series_country', to='characteristics.productcountry', verbose_name='Страна-производитель')),
                ('product_furniture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='series_furniture', to='characteristics.productfurniture', verbose_name='Тип мебели')),
            ],
            options={
                'verbose_name': 'Серия',
                'verbose_name_plural': 'Серии',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=127, verbose_name='title')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='url')),
                ('full_slug', models.CharField(blank=True, max_length=510, verbose_name='full_slug')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('meta_title', models.CharField(blank=True, max_length=127, verbose_name='meta_title')),
                ('meta_keywords', models.CharField(blank=True, max_length=127, verbose_name='meta_keywords')),
                ('meta_description', models.TextField(blank=True, max_length=510, verbose_name='meta_description')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Create date')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('image', models.ImageField(blank=True, upload_to='uploads/product/%Y-%m-%d/', verbose_name='image')),
                ('product_price', models.PositiveSmallIntegerField(default=0, verbose_name='Цена')),
                ('product_article', models.CharField(help_text='Обязательное поле, используется как КРАТКОЕ НАИМЕНОВАНИЕ', max_length=30, unique=True, verbose_name='Артикул (уникальный)')),
                ('product_code', models.CharField(help_text='Обязательное поле', max_length=30, unique=True, verbose_name='Код товара (уникальный)')),
                ('product_guarantee', models.CharField(blank=True, max_length=30, unique=True, verbose_name='Гарантия (год)')),
                ('product_top_table', models.CharField(blank=True, max_length=30, unique=True, verbose_name='Толщина столешницы')),
                ('product_production_time', models.CharField(blank=True, max_length=30, unique=True, verbose_name='Время производства')),
                ('product_delivery_time', models.CharField(blank=True, max_length=30, unique=True, verbose_name='Время доставки')),
                ('product_height', models.PositiveSmallIntegerField(default=0, verbose_name='Высота, мм')),
                ('product_width', models.PositiveSmallIntegerField(default=0, verbose_name='Ширина, мм')),
                ('product_length', models.PositiveSmallIntegerField(default=0, verbose_name='Длина, мм')),
                ('product_diameter', models.PositiveSmallIntegerField(default=0, verbose_name='Диаметр, мм')),
                ('product_weight', models.PositiveSmallIntegerField(default=0, verbose_name='Вес, кг')),
                ('gallery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='product_gallery', to='gallery.name', verbose_name='series_gallery')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='parent_product', to='product.series', verbose_name='parent_product')),
                ('product_brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='product_brand', to='characteristics.productbrand', verbose_name='Производитель (бренд)')),
                ('product_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='product_class', to='characteristics.productclass', verbose_name='Класс товара')),
                ('product_color', models.ManyToManyField(blank=True, related_name='product_color', to='characteristics.productcolor', verbose_name='Цвет')),
                ('product_country', models.ManyToManyField(blank=True, related_name='product_country', to='characteristics.productcountry', verbose_name='Страна-производитель')),
                ('product_furniture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='product_furniture', to='characteristics.productfurniture', verbose_name='Тип мебели')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
