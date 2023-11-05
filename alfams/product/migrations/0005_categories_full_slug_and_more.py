# Generated by Django 4.2.6 on 2023-10-27 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_categories_meta_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='full_slug',
            field=models.CharField(blank=True, max_length=510, verbose_name='full_slug'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='meta_description',
            field=models.TextField(blank=True, max_length=510, verbose_name='meta_description'),
        ),
    ]
