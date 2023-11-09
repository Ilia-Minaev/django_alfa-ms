# Generated by Django 4.2.6 on 2023-10-23 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='meta_description',
            field=models.CharField(blank=True, max_length=127, verbose_name='m_description'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=127, verbose_name='m_keywords'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='meta_title',
            field=models.CharField(blank=True, max_length=127, verbose_name='m_title'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='url'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=127, verbose_name='title'),
        ),
    ]