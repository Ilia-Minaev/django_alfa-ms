from typing import Any, Optional
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse_lazy

from blog.models import Articles, Portfolio
from blog.utils import PostMixin
from constants.utils import ConstantsMixin


class BlogView(ConstantsMixin, PostMixin, ListView):
    model = Articles
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context_page = self.get_page_context()
        context_constants = self.get_constants()
        context = context | context_constants

        context['title'] = 'Блог'
        #context['description'] = 'Блог'
        context['meta_title'] = 'Блог'
        context['meta_description'] = 'Блог'
        context['meta_keywords'] = 'Блог'

        context['breadcrumbs'] = [
            {
                'title': 'Главная',
                'full_slug': '/',
            },
            {
                'title': context['title'],
                'full_slug': reverse_lazy('blog:blog'),
            },
        ]

        return context

class ArticlesView(ConstantsMixin, PostMixin, ListView):
    model = Articles
    template_name = 'blog/articles.html'
    context_object_name = 'articles'

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context_page = self.get_page_context()
        context_constants = self.get_constants()
        context = context | context_constants

        context['title'] = 'Статьи'
        #context['description'] = 'Статьи'
        context['meta_title'] = 'Статьи'
        context['meta_description'] = 'Статьи'
        context['meta_keywords'] = 'Статьи'

        context['breadcrumbs'] = [
            {
                'title': 'Главная',
                'full_slug': '/',
            },
            {
                'title': 'Блог',
                'full_slug': reverse_lazy('blog:blog'),
            },
            {
                'title': context['title'],
                'full_slug': reverse_lazy('blog:articles'),
            },
        ]

        return context
    
class PortfolioView(ConstantsMixin, PostMixin, ListView):
    model = Portfolio
    template_name = 'blog/portfolio.html'
    context_object_name = 'portfolio'

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(is_published=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context_page = self.get_page_context()
        context_constants = self.get_constants()
        context = context | context_constants

        context['title'] = 'Портфолио'
        #context['description'] = 'Портфолио'
        context['meta_title'] = 'Портфолио'
        context['meta_description'] = 'Портфолио'
        context['meta_keywords'] = 'Портфолио'

        context['breadcrumbs'] = [
            {
                'title': 'Главная',
                'full_slug': '/',
            },
            {
                'title': 'Блог',
                'full_slug': reverse_lazy('blog:blog'),
            },
            {
                'title': context['title'],
                'full_slug': reverse_lazy('blog:portfolio'),
            },
        ]

        return context
    
class ArticleSingleView(ConstantsMixin, PostMixin, ListView):
    model = Articles
    template_name = 'blog/articles_single.html'
    context_object_name = 'articles'

    def get_queryset(self) -> QuerySet[Any]:
        return self.get_post()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_date_created = self.get_post().date_created
        
        context_page = self.get_meta_post_single()
        context_constants = self.get_constants()
        context = context | context_page | context_constants

        context['breadcrumbs'] = [
            {
                'title': 'Главная',
                'full_slug': '/',
            },
            {
                'title': 'Блог',
                'full_slug': reverse_lazy('blog:blog'),
            },
            {
                'title': 'Статьи',
                'full_slug': reverse_lazy('blog:articles'),
            },
            {
                'title': self.get_post().title,
                'full_slug': self.get_post().get_absolute_url(),
            },
        ]

        context['next_object'] = self.get_next_object(current_date_created)
        context['previous_object'] = self.get_previous_object(current_date_created)

        return context
    
class PortfolioSingleView(ConstantsMixin, PostMixin, ListView):
    model = Portfolio
    template_name = 'blog/portfolio_single.html'
    context_object_name = 'portfolio'

    def get_queryset(self) -> QuerySet[Any]:
        return self.get_post()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_date_created = self.get_post().date_created

        context_page = self.get_meta_post_single()
        context_constants = self.get_constants()
        context = context | context_page | context_constants

        context['gallery'] = self.get_gallery()

        context['breadcrumbs'] = [
            {
                'title': 'Главная',
                'full_slug': '/',
            },
            {
                'title': 'Блог',
                'full_slug': reverse_lazy('blog:blog'),
            },
            {
                'title': 'Портфолио',
                'full_slug': reverse_lazy('blog:portfolio'),
            },
            {
                'title': self.get_post().title,
                'full_slug': self.get_post().get_absolute_url(),
            },
        ]
        
        context['next_object'] = self.get_next_object(current_date_created)
        context['previous_object'] = self.get_previous_object(current_date_created)

        return context