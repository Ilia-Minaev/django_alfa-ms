
from django.urls import path, include

from product.views import CategoryView, SubCategoryView


app_name = 'product'

urlpatterns = [
    path('', CategoryView.as_view(), name='category'),
    path('<slug:category_slug_1>/', SubCategoryView.as_view(), name='category_1'),
    path('<slug:category_slug_1>/<slug:category_slug_2>/', SubCategoryView.as_view(), name='category_2'),
    path('<slug:category_slug_1>/<slug:category_slug_2>/<slug:category_slug_3>/', SubCategoryView.as_view(), name='category_3'),
]