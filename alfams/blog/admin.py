from django.contrib import admin

from blog.models import Articles, Portfolio
from blog.forms import ArticlesAdminForm, PortfolioAdminForm



class BlogAdmin(admin.ModelAdmin):
    list_display = ('is_published', 'title', 'show_img')
    list_display_links = ('title',)
    fields = ('is_published', 'title', 'slug', 'show_img', 'image', 'description', 'meta_title',
              'meta_keywords', 'meta_description', 'gallery', 'date_created', 'date_updated')
    readonly_fields = ('show_img', 'date_created', 'date_updated')
    prepopulated_fields = {'slug': ('title',)}


class ArticlesAdmin(BlogAdmin):
    form = ArticlesAdminForm


class PortfolioAdmin(BlogAdmin):
    form = PortfolioAdminForm


admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Portfolio, PortfolioAdmin)