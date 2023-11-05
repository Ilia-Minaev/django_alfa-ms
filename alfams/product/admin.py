from django.contrib import admin

from product.models import Categories, Series, Products
from product.forms import CategoriesAdminForm



class CategoriesAdmin(admin.ModelAdmin):
    form = CategoriesAdminForm

    list_display = ('is_published', 'title', 'parent', 'level', 'show_icon')
    list_display_links = ('title',)
    list_filter = ('parent',)
    fields = ('is_published', 'title', 'slug', 'full_slug', 'parent', 'children', 'level', 
              'show_icon', 'icon', 'show_img', 'image', 'description', 'meta_title',
              'meta_keywords', 'meta_description', 'date_created', 'date_updated')
    readonly_fields = ('level', 'children', 'full_slug', 'show_icon', 'show_img', 'date_created', 'date_updated')

    prepopulated_fields = {'slug': ('title',)}

class SeriesAdmin(admin.ModelAdmin):
    form = CategoriesAdminForm

    list_display = ('is_published', 'title', 'show_img')
    list_display_links = ('title',)
    fields = ('is_published', 'title', 'slug', 'full_slug', 
              'show_img', 'image', 'description', 'meta_title',
              'meta_keywords', 'meta_description', 'date_created', 'date_updated')
    readonly_fields = ('full_slug', 'show_img', 'date_created', 'date_updated')

    prepopulated_fields = {'slug': ('title',)}

class ProductsAdmin(admin.ModelAdmin):
    form = CategoriesAdminForm

    list_display = ('is_published', 'title', 'parent', 'show_img')
    list_display_links = ('title',)
    list_filter = ('parent',)
    fields = ('is_published', 'title', 'slug', 'full_slug', 'parent', 
              'show_img', 'image', 'description', 'meta_title',
              'meta_keywords', 'meta_description', 'date_created', 'date_updated')
    readonly_fields = ('full_slug', 'show_img', 'date_created', 'date_updated')
    
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Products, ProductsAdmin)