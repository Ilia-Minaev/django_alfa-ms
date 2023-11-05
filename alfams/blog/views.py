from typing import Any, Optional
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView

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
        context['description'] = 'Блог'
        context['meta_title'] = 'Блог'
        context['meta_description'] = 'Блог'
        context['meta_keywords'] = 'Блог'

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
        context['description'] = 'Статьи'
        context['meta_title'] = 'Статьи'
        context['meta_description'] = 'Статьи'
        context['meta_keywords'] = 'Статьи'

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
        context['description'] = 'Портфолио'
        context['meta_title'] = 'Портфолио'
        context['meta_description'] = 'Портфолио'
        context['meta_keywords'] = 'Портфолио'

        return context
    
class ArticleSingleView(ConstantsMixin, PostMixin, ListView):
    model = Articles
    template_name = 'blog/articles_single.html'
    context_object_name = 'articles'

    def get_queryset(self) -> QuerySet[Any]:
        return self.get_post()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.obj
        current_date_created = obj.date_created
        
        context_page = self.get_meta_post_single()
        context_constants = self.get_constants()
        context = context | context_page | context_constants

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
        obj = self.obj
        current_date_created = obj.date_created

        context_page = self.get_meta_post_single()
        context_constants = self.get_constants()
        context = context | context_page | context_constants

        context['gallery'] = self.get_gallery()
        
        context['next_object'] = self.get_next_object(current_date_created)
        context['previous_object'] = self.get_previous_object(current_date_created)

        return context