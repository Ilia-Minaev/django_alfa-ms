
from django.urls import path, include, re_path

from product.views import CategoryView, SubCategoryView, SingleSeries


app_name = 'product_ex'

urlpatterns = [
    #path('', SingleSeries.as_view(), name='single_serie'),
    #re_path(r'^<slug:serie_slug>/', SingleSeries.as_view(), name='single_serie__'),
    #re_path(r'?/(?P<slug>[\w-]+)/$', SingleSeries.as_view()),
    re_path(r'^(?P<slug>[\w-]+)/$', SingleSeries.as_view()),
    re_path(r'^(?P<slug2>[\w-]+)/(?P<slug>[\w-]+)/$', SingleSeries.as_view()),
    re_path(r'^(?P<slug3>[\w-]+)/(?P<slug2>[\w-]+)/(?P<slug>[\w-]+)/$', SingleSeries.as_view()),
    re_path(r'^(?P<slug4>[\w-]+)/(?P<slug3>[\w-]+)/(?P<slug2>[\w-]+)/(?P<slug>[\w-]+)/$', SingleSeries.as_view()),
]


"""
urlpatterns = [


    #re_path('<slug:category_slug_1>/<slug:category_slug_2>/<slug:category_slug_3>/', SubCategoryView.as_view(), name='category_3'),
    #path('<slug:category_slug_1>/<slug:serie_slug_1>/', SingleSeries.as_view(), name='serie_1'),
    #re_path('<slug:category_slug_1>/<slug:category_slug_2>/', SubCategoryView.as_view(), name='category_2'),
    re_path('', CategoryView.as_view(), name='category'),
    re_path('<slug:category_slug_1>/', SubCategoryView.as_view(), name='category_1'),
]
"""