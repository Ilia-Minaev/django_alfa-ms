# Generated by Django 4.2.6 on 2023-10-23 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_categories_options_alter_categories_children_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ('level', 'parent_id'), 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]
