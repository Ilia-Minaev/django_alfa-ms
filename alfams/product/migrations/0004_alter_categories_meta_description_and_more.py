# Generated by Django 4.2.6 on 2023-10-23 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_categories_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='meta_description',
            field=models.TextField(blank=True, max_length=127, verbose_name='meta_description'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=127, verbose_name='meta_keywords'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='meta_title',
            field=models.CharField(blank=True, max_length=127, verbose_name='meta_title'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='url'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='title',
            field=models.CharField(max_length=127, verbose_name='title'),
        ),
    ]
