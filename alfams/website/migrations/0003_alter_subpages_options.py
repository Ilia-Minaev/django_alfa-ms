# Generated by Django 4.2.6 on 2023-10-31 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_remove_pages_childrens_subpages_parent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subpages',
            options={'ordering': ('parent_id',), 'verbose_name': 'Доп.Страницы', 'verbose_name_plural': 'Доп.Страницы'},
        ),
    ]
