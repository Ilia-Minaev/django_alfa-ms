# Generated by Django 4.2.6 on 2023-11-14 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characteristics', '0002_productbrand_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcolor',
            name='title',
            field=models.CharField(max_length=30, verbose_name='Цвет'),
        ),
    ]
