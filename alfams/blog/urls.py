
from django.urls import path
from django.views.decorators.cache import cache_page

from blog.views import BlogView, ArticlesView, PortfolioView, ArticleSingleView, PortfolioSingleView


app_name = 'blog'
cache_time = 60*60*24

urlpatterns = [
    path('', cache_page(cache_time)(BlogView.as_view()), name='blog'),
    path('articles/', cache_page(cache_time)(ArticlesView.as_view()), name='articles'),
    path('portfolio/', cache_page(cache_time)(PortfolioView.as_view()), name='portfolio'),
    path('articles/<slug:post_slug>/', cache_page(cache_time)(ArticleSingleView.as_view()), name='article_single'),
    path('portfolio/<slug:post_slug>/', cache_page(cache_time)(PortfolioSingleView.as_view()), name='portfolio_single'),
]