# Generated by Django 4.2.5 on 2023-10-04 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=128, verbose_name='title')),
                ('slug', models.SlugField(max_length=256, unique=True, verbose_name='url')),
                ('image', models.ImageField(blank=True, upload_to='uploads/blog/%Y-%m-%d/', verbose_name='image')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('meta_title', models.CharField(blank=True, max_length=128, verbose_name='m_title')),
                ('meta_keywords', models.CharField(blank=True, max_length=128, verbose_name='m_keywords')),
                ('meta_description', models.CharField(blank=True, max_length=128, verbose_name='m_description')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Create date')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('blog_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.blog')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
            bases=('blog.blog',),
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('blog_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.blog')),
            ],
            options={
                'verbose_name': 'Портфолио',
                'verbose_name_plural': 'Портфолио',
            },
            bases=('blog.blog',),
        ),
    ]