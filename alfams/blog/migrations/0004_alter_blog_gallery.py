# Generated by Django 4.2.6 on 2023-10-31 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_alter_images_options_alter_name_options'),
        ('blog', '0003_blog_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='blog_gallery', to='gallery.name', verbose_name='blog_gallery'),
        ),
    ]
