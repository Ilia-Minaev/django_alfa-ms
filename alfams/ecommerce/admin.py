from django.contrib import admin


from ecommerce.models import CurrencyRates, Course


class CurrencyRatesAdmin(admin.ModelAdmin):
    list_display = ('title', 'rate',)
    list_display_links = ('title',)
    #list_filter = ('parent',)
    fields = ('title', 'rate',)
    #readonly_fields = ('level', 'children', 'full_slug', 'show_icon', 'show_img', 'date_created', 'date_updated')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('parent_series', 'parent_brand', 'parent_rate', 'extra_charge', 'discount_real', 'discount_fake')
    list_display_links = ('parent_series', 'parent_brand',)
    list_filter = ('parent_series',)
    fields = ('parent_series', 'parent_brand', 'parent_rate', 'extra_charge', 'discount_real', 'discount_fake')
    #readonly_fields = ('level', 'children', 'full_slug', 'show_icon', 'show_img', 'date_created', 'date_updated')

    #prepopulated_fields = {'slug': ('title',)}



admin.site.register(CurrencyRates, CurrencyRatesAdmin)
admin.site.register(Course, CourseAdmin)