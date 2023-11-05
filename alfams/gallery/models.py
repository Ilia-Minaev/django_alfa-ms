from django.db import models
from django.utils.safestring import mark_safe

class Name(models.Model):
    is_published = models.BooleanField(default=True)
    is_3d = models.BooleanField(default=False)
    title = models.CharField(max_length=127, blank=False, verbose_name='title')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Имя галереи'
        verbose_name_plural = 'Имя галереи'
        ordering = ('title',)


class Images(models.Model):
    is_published = models.BooleanField(default=True)
    parent = models.ForeignKey(Name, blank=False, related_name='parent_gallery', verbose_name='parent_gallery', on_delete=models.PROTECT)
    image = models.ImageField(upload_to='uploads/gallery/%Y-%m-%d/', blank=False, verbose_name='image')

    def show_img(self):
        if self.image:
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100" height="100"></a>'.format(self.image.url))
        else:
            return '<div>No photo</div>'
        
    show_img.short_description = 'Image'
    show_img.allow_tags = True

    #def __str__(self):
    #    return self.pk
    
    class Meta:
        verbose_name = 'Картинки'
        verbose_name_plural = 'Картинки'
        ordering = ('parent',)