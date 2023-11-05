from django.contrib import admin

from gallery.models import Name, Images


class NameAdmin(admin.ModelAdmin):

    list_display = ('is_published', 'is_3d', 'title',)
    list_display_links = ('title',)


class ImagesAdmin(admin.ModelAdmin):

    list_display = ('is_published', 'id' ,'parent', 'show_img')
    list_display_links = ('id', 'parent')
    list_filter = ('parent',)
    fields = ('is_published', 'parent', 'show_img', 'image')

    readonly_fields = ('show_img',)


admin.site.register(Name, NameAdmin)
admin.site.register(Images, ImagesAdmin)