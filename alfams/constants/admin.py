from django.contrib import admin

from constants.models import Constants, Slider
#from constants.forms import PhoneAdminForm

class ConstantsAdmin(admin.ModelAdmin):
    list_display = ('site_name',)
    list_display_links = ('site_name',)
    fields = (
        'site_name', 'address', 'show_img', 'logo', 'email',
        'phone1', 'phone2', 'facebook', 'twitter',
        'instagram', 'linkedin', 'youtube', 'vk',
    )
    readonly_fields = ('show_img',)

    def has_add_permission(self, request, obj=None):
        return False
    

class SliderAdmin(admin.ModelAdmin):
    list_display = ('action', 'title', 'show_img')
    list_display_links = ('title',)
    fields = ('action', 'title', 'description', 'show_img', 'image', 'button_title', 'button_slug')
    readonly_fields = ('show_img',)


admin.site.register(Constants, ConstantsAdmin)
admin.site.register(Slider, SliderAdmin)