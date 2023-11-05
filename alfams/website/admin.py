from django.contrib import admin

from website.models import Pages, SubPages
from website.forms import PagesAdminForm


class PagesAdmin(admin.ModelAdmin):
    form = PagesAdminForm

    list_display = ('is_published', 'title', 'date_updated', 'is_header', 'is_footer')
    list_display_links = ('title',)
    readonly_fields = ('date_created', 'date_updated')

    prepopulated_fields = {'slug': ('title',)}

class SubPagesAdmin(admin.ModelAdmin):
    form = PagesAdminForm

    list_display = ('is_published', 'title', 'date_updated', 'parent', 'show_img')
    list_display_links = ('title',)
    list_filter = ('parent',)
    fields = ('is_published', 'title', 'slug', 'parent', 'show_img', 
              'image', 'description', 'meta_title',
              'meta_keywords', 'meta_description', 'date_created', 'date_updated')
    readonly_fields = ('show_img', 'date_created', 'date_updated')

    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Pages, PagesAdmin)
admin.site.register(SubPages, SubPagesAdmin)