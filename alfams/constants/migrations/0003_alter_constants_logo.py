# Generated by Django 4.2.5 on 2023-10-14 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constants', '0002_alter_constants_options_alter_slider_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constants',
            name='logo',
            field=models.FileField(blank=True, help_text='svg or img', upload_to='uploads/logo/', verbose_name='logo'),
        ),
    ]
