from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

from gallery.models import Name

class Blog(models.Model):
    is_published = models.BooleanField(default=True)
    title = models.CharField(max_length=127, blank=False, verbose_name='title')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='url')
    image = models.ImageField(upload_to='uploads/blog/%Y-%m-%d/', blank=True, verbose_name='image')
    description = models.TextField(blank=True, verbose_name='description')
    meta_title = models.CharField(max_length=127, blank=True, verbose_name='m_title')
    meta_keywords = models.CharField(max_length=127, blank=True, verbose_name='m_keywords')
    meta_description = models.CharField(max_length=127, blank=True, verbose_name='m_description')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Create date')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Update date')
    gallery = models.ForeignKey(Name, blank=True, null=True, related_name='blog_gallery', verbose_name='blog_gallery', on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.title
    
    def show_img(self):
        if self.image:
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100" height="100"></a>'.format(self.image.url))
        else:
            return '<div>No photo</div>'
        
    show_img.short_description = 'Image'
    show_img.allow_tags = True

    def __str__(self):
        return self.title


class Articles(Blog):
    def get_absolute_url(self):
        return reverse('blog:article_single', kwargs={'post_slug': self.slug})
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Portfolio(Blog):
    def get_absolute_url(self):
        return reverse('blog:portfolio_single', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'