from typing import Any, Optional
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, RedirectView

from website.models import Pages, SubPages
from product.models import Categories
from website.utils import WebsiteMixin
from constants.utils import ConstantsMixin


class HomeView(ConstantsMixin, WebsiteMixin, ListView):
    model = Pages
    template_name = 'website/index.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Categories.objects.filter(parent=None).filter(is_published=True)

    def get_context_data(self, **kwargs):
        self.kwargs['page_slug'] = 'home'
        context = super().get_context_data(**kwargs)
        context_page = self.get_page_context()
        context_constants = self.get_constants()
        context = context | context_page | context_constants

        return context


class HomeRedirectView(RedirectView):
    url = reverse_lazy('pages:home')


class PagesView(ConstantsMixin, WebsiteMixin, ListView):
    model = Pages
    template_name = 'website/pages.html'
    context_object_name = 'pages'

    def get_queryset(self):
        parent_id = self.get_page_obj().pk
        return SubPages.objects.filter(parent=parent_id).filter(is_published=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_page = self.get_page_context()
        context_constants = self.get_constants()
        context = context | context_page | context_constants

        #context['breadcrumbs'] = self.get_breadcrumbs_path()
        context['breadcrumbs'] = self.get_breadcrumbs()

        return context
    

class SubPagesView(ConstantsMixin, WebsiteMixin, ListView):
    model = SubPages
    template_name = 'website/pages.html'
    #context_object_name = 'pages'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        url = self.request.get_full_path()[1:-1].split('/')
        if url[0] == url[1]:
            raise Http404('Bad url')
        return super().get(request, *args, **kwargs)

    #def get_queryset(self):
        #return super().get_queryset().filter(parent=None).filter(is_published=True)
    
    def get_context_data(self, **kwargs):
        #self.kwargs['page_slug'] = self.kwargs['page_slug_1']

        context = super().get_context_data(**kwargs)
        context_page = self.get_page_context()
        context_constants = self.get_constants()
        context = context | context_page | context_constants

        #context['breadcrumbs'] = self.get_breadcrumbs_path()
        context['breadcrumbs'] = self.get_breadcrumbs()
        
        return context
