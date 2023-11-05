
from django.urls import path

from blog.views import BlogView, ArticlesView, PortfolioView, ArticleSingleView, PortfolioSingleView


app_name = 'blog'

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('articles/', ArticlesView.as_view(), name='articles'),
    path('portfolio/', PortfolioView.as_view() , name='portfolio'),
    path('articles/<slug:post_slug>/', ArticleSingleView.as_view(), name='article_single'),
    path('portfolio/<slug:post_slug>/', PortfolioSingleView.as_view() , name='portfolio_single'),
]