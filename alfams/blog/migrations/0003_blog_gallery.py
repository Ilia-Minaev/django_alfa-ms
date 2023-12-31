# Generated by Django 4.2.6 on 2023-10-31 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_alter_images_options_alter_name_options'),
        ('blog', '0002_alter_blog_meta_description_alter_blog_meta_keywords_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='gallery',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, related_name='blog_gallery', to='gallery.name', verbose_name='blog_gallery'),
            preserve_default=False,
        ),
    ]
