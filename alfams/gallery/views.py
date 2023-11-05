
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from gallery.models import Images
from gallery.forms import GalltryForm
from constants.utils import ConstantsMixin


class GalleryView(LoginRequiredMixin, ConstantsMixin, CreateView):
    #model = Images
    template_name = 'gallery/index.html'
    #context_object_name = 'categories'
    form_class = GalltryForm
    success_url = '/gallery/'
     
    def form_valid(self, form):
        images = form.files.getlist('image')

        for item in images:
            new_form = Images()
            new_form.parent = form.cleaned_data["parent"]
            new_form.image = item
            new_form.save()

        return redirect(self.success_url)

    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context_page = self.get_page_context()
        context_constants = self.get_constants()
        context = context | context_constants

        context['title'] = 'Галерея'
        context['description'] = 'Галерея'
        context['meta_title'] = 'Галерея'
        context['meta_description'] = 'Галерея'
        context['meta_keywords'] = 'Галерея'
        
        return context
    