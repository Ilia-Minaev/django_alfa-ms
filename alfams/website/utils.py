from website.models import PagesBaseModel

class WebsiteMixin:
    obj = None

    def get_page_obj(self, **kwargs):
        self.obj = super().get_queryset().get(slug=self.kwargs.get('page_slug'))
        return self.obj
    
    def get_breadcrumbs_path(self, **kwargs):
        full_url = self.request.get_full_path()
        url = full_url[1:-1].split('/')
        path_nested = len(url)

        category_path = 'website/breadcrumbs/_' + str(path_nested) + '.html'
        category_dict = {
            'category_path': category_path,
            'category': {
                'title': 'Каталог',
                'full_slug': '/category/',
            },
            'url': ''
        }

        for i in range(0 ,int(path_nested) + 1):
            try:
                url_category = PagesBaseModel.objects.get(slug=url[i])
                cat = 'category_' + str(i)
                category_dict[cat] = {}
                category_dict[cat]['title'] = url_category.title
                if i == 0:
                    category_dict[cat]['full_slug'] = '/' + url[0] + '/'
                else:
                    category_dict[cat]['full_slug'] = full_url
            except:
                pass

        return category_dict

    def get_page_context(self, **kwargs):
        context = kwargs
        if self.obj == None:
            page = self.get_page_obj()
        else:
            page = self.obj

        context['title'] = page.title
        context['description'] = page.description
        context['meta_title'] = page.meta_title or page.title
        context['meta_description'] = page.meta_description or page.title
        context['meta_keywords'] = page.meta_keywords or page.title

        return context