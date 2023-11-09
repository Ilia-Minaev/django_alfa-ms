from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

class PagesBaseModel(models.Model):
    is_published = models.BooleanField(default=True)
    title = models.CharField(max_length=127, blank=False, verbose_name='title')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='url')
    image = models.ImageField(upload_to='uploads/pages/%Y-%m-%d/', blank=True, verbose_name='image')
    description = models.TextField(blank=True, null=True, verbose_name='description')
    meta_title = models.CharField(max_length=127, blank=True, verbose_name='meta_title')
    meta_keywords = models.CharField(max_length=127, blank=True, verbose_name='meta_keywords')
    meta_description = models.TextField(max_length=127, blank=True, verbose_name='meta_description')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Create date')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Update date')
    is_header = models.BooleanField(default=True)
    is_footer = models.BooleanField(default=True)

    def show_img(self):
        if self.image:
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100" height="100"></a>'.format(self.image.url))
        else:
            return mark_safe('<div style="color:red">No photo</div>')
        
    show_img.short_description = 'Image'
    show_img.allow_tags = True

    def __str__(self):
        return self.title


class Pages(PagesBaseModel):
    def get_absolute_url(self):
        return reverse('title', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = 'Страницы'
        verbose_name_plural = 'Страницы'


class SubPages(PagesBaseModel):
    parent = models.ForeignKey(Pages, blank=True, null=True, related_name='+', verbose_name='parent_category', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Доп.Страницы'
        verbose_name_plural = 'Доп.Страницы'
        ordering = ('parent_id',)
