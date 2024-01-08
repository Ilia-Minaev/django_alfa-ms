from django.contrib import admin


from ecommerce.models import CurrencyRates, Course, Order
from ecommerce.forms import OrderAdminForm


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

class OrderAdmin(admin.ModelAdmin):
    form = OrderAdminForm
    
    list_display = ('id', 'order_type', 'name', 'email', 'phone', 'date_created',)
    list_display_links = ('id', 'order_type', 'name',)
    fields = ('id', 'name', 'email', 'phone', 'street', 'city', 'payment_method', 'comment', 'order', 'order_type', 'date_created', 'date_updated',)
    readonly_fields = ('id', 'order_type', 'date_created', 'date_updated')

    list_filter = ('order_type',)


admin.site.register(CurrencyRates, CurrencyRatesAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Order, OrderAdmin)