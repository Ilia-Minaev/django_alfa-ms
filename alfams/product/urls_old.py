
from django.urls import path, include, re_path

from product.views import CategoryView, SubCategoryView, SingleSeries


app_name = 'product'

urlpatterns = [
    path('', CategoryView.as_view(), name='category'),
    path('<slug:category_slug_1>/', SubCategoryView.as_view(), name='category_1'),
    path('<slug:category_slug_1>/<slug:category_slug_2>/', SubCategoryView.as_view(), name='category_2'),

    #path('<slug:category_slug_1>/<slug:serie_slug_1>/', SingleSeries.as_view(), name='serie_1'),

    path('<slug:category_slug_1>/<slug:category_slug_2>/<slug:category_slug_3>/', SubCategoryView.as_view(), name='category_3'),
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