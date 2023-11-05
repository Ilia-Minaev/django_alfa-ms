from django.contrib import admin

from characteristics.models import ProductBrand, ProductCountry, ProductClass, ProductFurniture, ProductMaterial, ProductColor

class CharacteristicsBaseAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    fields = ('title',)


class ProductBrandAdmin(CharacteristicsBaseAdmin):
    pass

class ProductCountryAdmin(CharacteristicsBaseAdmin):
    list_display = ('title', 'show_img')
    fields = ('title', 'show_img', 'image')
    readonly_fields = ('show_img',)

class ProductClassAdmin(CharacteristicsBaseAdmin):
    def has_add_permission(self, request, obj=None):
        return False

class ProductFurnitureAdmin(CharacteristicsBaseAdmin):
    pass

class ProductMaterialAdmin(CharacteristicsBaseAdmin):
    pass

class ProductColorAdmin(CharacteristicsBaseAdmin):
    list_display = ('title', 'parent', 'show_img')
    list_filter = ('parent',)
    fields = ('title', 'parent', 'show_img', 'image')
    readonly_fields = ('show_img',)



admin.site.register(ProductBrand, ProductBrandAdmin)
admin.site.register(ProductCountry, ProductCountryAdmin)
admin.site.register(ProductClass, ProductClassAdmin)
admin.site.register(ProductFurniture, ProductFurnitureAdmin)
admin.site.register(ProductMaterial, ProductMaterialAdmin)
admin.site.register(ProductColor, ProductColorAdmin)