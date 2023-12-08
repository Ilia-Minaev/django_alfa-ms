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
    fields = (
        'is_published', 'title', 'slug', 'full_slug', 
        'show_img', 'image', 'description',

        'product_call_us', 'product_recommended',

        'product_price',

        'product_article', 'product_code',
        'product_guarantee', 'product_top_table',
        'product_production_time', 'product_delivery_time',
        
        'parent', 'product_brand', 'product_class', 'product_furniture',
        
        'product_country', 'product_color',

        'gallery',
              
        'meta_title', 'meta_keywords', 'meta_description', 'date_created', 'date_updated')
    readonly_fields = ('full_slug', 'show_img', 'date_created', 'date_updated')

    prepopulated_fields = {'slug': ('product_article',)}

class ProductsAdmin(admin.ModelAdmin):
    form = CategoriesAdminForm

    list_display = ('is_published', 'product_code', 'product_code_color', 'title', 'parent', 'product_brand', 'product_color', 'show_img')
    list_display_links = ('title',)
    list_filter = ('parent',)
    fields = (
        'is_published', 'title', 'slug', 'full_slug', 
        'show_img', 'image', 'description',



        'product_price',

        'product_article', 'product_code', 'product_code_color',
        'product_guarantee', 'product_top_table',
        'product_production_time', 'product_delivery_time',
        
        'parent', 'product_brand', 'product_class', 'product_furniture',
        
        'product_country', 'product_color',

        'product_height', 'product_width', 'product_length',

        'gallery',
              
        'meta_title', 'meta_keywords', 'meta_description', 'date_created', 'date_updated')
    readonly_fields = ('full_slug', 'show_img', 'date_created', 'date_updated')
    
    prepopulated_fields = {'slug': ('product_code',)}
    ordering = ('product_brand', 'product_code')
    save_as = True


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Products, ProductsAdmin)