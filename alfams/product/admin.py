from django.contrib import admin
from django.urls import path
from django.shortcuts import render
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
from product.utils import Import_Upload
class SeriesAdmin(admin.ModelAdmin):
    #change_list_template = "templates/admin/monitor_change_list.html"

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
        
        'parent', 'product_brand', 'product_class', 
        #'product_furniture',
        
        'product_country', 
        #'product_color',

        'gallery', 'file_import',
              
        'meta_title', 'meta_keywords', 'meta_description', 'date_created', 'date_updated')
    readonly_fields = ('full_slug', 'show_img', 'date_created', 'date_updated')

    #prepopulated_fields = {'slug': ('product_article',)}
    
    def get_urls(self):
        urls = super().get_urls()
        urls.insert(-1, path('import-upload/', self.import_upload))
        return urls
    
    def import_upload(self, request):
        if request.method == 'POST':
            
            #from product.utils import Import_Upload
            file = request.FILES['import']
            import_file = Import_Upload()
            import_file.start_import(file=file)
            #self.start_import(file=file)


        return render(request, 'admin/import_form.html',
                      #{'form': form}
                      )

    

class ProductsAdmin(admin.ModelAdmin):
    form = CategoriesAdminForm

    list_display = (
        'is_published', 'product_code', 'product_code_color', 'title', 'parent', 'product_brand', 'get_product_material_color', 'show_img'
    )
    list_display_links = ('product_code', 'product_code_color', 'title', )
    list_filter = ('parent',)
    fields = (
        'is_published', 'title', 'slug', 'full_slug', 
        'show_img', 'image', 'description',

        'product_price',

        'product_article', 'product_code', 'product_code_color',
        'product_guarantee', 'product_top_table',
        'product_production_time', 'product_delivery_time',
        
        'parent', 'product_brand', 'product_class', 'product_furniture',
        
        'product_country', 'product_color', 'get_product_material_color',

        'product_height', 'product_width', 'product_length',

        'gallery',
              
        'meta_title', 'meta_keywords', 'meta_description', 'date_created', 'date_updated')
    
    readonly_fields = (
        'slug','full_slug', 'show_img', 'date_created', 'date_updated', 'product_code_color', 'get_product_material_color',
    )
    
    #prepopulated_fields = {'slug': ('product_code',)}
    ordering = ('product_brand', 'product_code')
    save_as = True


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Products, ProductsAdmin)