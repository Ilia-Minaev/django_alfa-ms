
from django.urls import path, include, re_path

from product.views import (
    ShopRedirectView, CategoryView, SeriesSingleView, ProductSingleView,
    SearchView
)


app_name = 'shop'

urlpatterns = [
    path('', ShopRedirectView.as_view(), name='shop'),
    
    path('category/', CategoryView.as_view(), name='category'),
    re_path(r'^category/(?P<slug>[\w-]+)/$', CategoryView.as_view()),
    re_path(r'^category/(?P<slug2>[\w-]+)/(?P<slug>[\w-]+)/$', CategoryView.as_view()),

    path('series/', ShopRedirectView.as_view(), name='series'),
    re_path(r'^series/(?P<slug>[\w-]+)/$', SeriesSingleView.as_view()),
    re_path(r'^series/(?P<slug2>[\w-]+)/(?P<slug>[\w-]+)/$', SeriesSingleView.as_view()),
    re_path(r'^series/(?P<slug3>[\w-]+)/(?P<slug2>[\w-]+)/(?P<slug>[\w-]+)/$', SeriesSingleView.as_view()),
    re_path(r'^series/(?P<slug4>[\w-]+)/(?P<slug3>[\w-]+)/(?P<slug2>[\w-]+)/(?P<slug>[\w-]+)/$', SeriesSingleView.as_view()),

    path('product/', ShopRedirectView.as_view(), name='product'),
    re_path(r'^product/(?P<slug>[\w-]+)/$', ProductSingleView.as_view()),
    re_path(r'^product/(?P<slug2>[\w-]+)/(?P<slug>[\w-]+)/$', ProductSingleView.as_view()),
    re_path(r'^product/(?P<slug3>[\w-]+)/(?P<slug2>[\w-]+)/(?P<slug>[\w-]+)/$', ProductSingleView.as_view()),
    re_path(r'^product/(?P<slug4>[\w-]+)/(?P<slug3>[\w-]+)/(?P<slug2>[\w-]+)/(?P<slug>[\w-]+)/$', ProductSingleView.as_view()),

    path('search/', SearchView.as_view(), name='search'),

    #re_path(r'^(?P<slug>[\w-]+)/$', SingleSeries.as_view()),
    #re_path(r'^(?P<slug2>[\w-]+)/(?P<slug>[\w-]+)/$', SingleSeries.as_view()),
    #re_path(r'^(?P<slug3>[\w-]+)/(?P<slug2>[\w-]+)/(?P<slug>[\w-]+)/$', SingleSeries.as_view()),
    #re_path(r'^(?P<slug4>[\w-]+)/(?P<slug3>[\w-]+)/(?P<slug2>[\w-]+)/(?P<slug>[\w-]+)/$', SingleSeries.as_view()),
]
