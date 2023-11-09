# Generated by Django 4.2.5 on 2023-10-20 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=128, verbose_name='title')),
                ('slug', models.SlugField(max_length=256, unique=True, verbose_name='url')),
                ('level', models.PositiveSmallIntegerField(default=0)),
                ('icon', models.FileField(blank=True, help_text='svg or img, 50x50px', upload_to='uploads/category/%Y-%m-%d/', verbose_name='icon')),
                ('image', models.ImageField(blank=True, upload_to='uploads/category/%Y-%m-%d/', verbose_name='image')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('meta_title', models.CharField(blank=True, max_length=128, verbose_name='meta_title')),
                ('meta_keywords', models.CharField(blank=True, max_length=128, verbose_name='meta_keywords')),
                ('meta_description', models.TextField(blank=True, max_length=128, verbose_name='meta_description')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Create date')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('children', models.ManyToManyField(blank=True, related_name='children_category', to='product.categories')),
                ('parent', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_category', to='product.categories')),
            ],
            options={
                'verbose_name': 'Страницы',
                'verbose_name_plural': 'Страницы',
            },
        ),
    ]