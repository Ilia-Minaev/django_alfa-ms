from website.models import PagesBaseModel, Pages

class WebsiteMixin:
    obj = None

    def get_page_obj(self, **kwargs):
        if self.obj:
            return self.obj
        self.obj = super().get_queryset().get(slug=self.kwargs.get('page_slug'))
        return self.obj
    
    def get_breadcrumbs(self, **kwargs):
        breadcrumbs_list = []
        page = self.get_page_obj()
        parent = None

        breadcrumbs_list.append({
            'title': 'Главная',
            'full_slug': '/'
        })
        if self.kwargs.get('page_slug_1'):
            parent = Pages.objects.get(slug=self.kwargs.get('page_slug_1'))
            breadcrumbs_list.append({
                'title': parent.title,
                'full_slug': f'/{parent.slug}/'
            })
        breadcrumbs_list.append({
            'title': page.title,
            'full_slug': f'/{parent.slug}/{page.slug}/' if parent else f'/{page.slug}/'
        })
        return breadcrumbs_list

    def get_page_context(self, **kwargs):
        context = kwargs
        page = self.get_page_obj()

        context['title'] = page.title
        context['description'] = page.description
        context['meta_title'] = page.meta_title or page.title
        context['meta_description'] = page.meta_description or page.title
        context['meta_keywords'] = page.meta_keywords or page.title

        return context