from product.models import Categories, Series, Products

class ProductMixin():

    obj = None

    def get_category(self, **kwargs):
        if self.obj:
            return self.obj
        else:
            url = self.request.get_full_path()[1:-1].split('/')[-1]
            self.obj = super().get_queryset().get(slug=url)
            return self.obj
    
    def get_breadcrumbs_cat(self, **kwargs):
        url = self.request.get_full_path()[1:-1].split('/')
        path_nested = len(url)

        category_path = 'product/breadcrumbs/_' + str(path_nested) + '.html'
        category_dict = {
            'category_path': category_path,
            'category': {
                'title': 'Каталог',
                'full_slug': '/category/',
            },
        }

        for i in range(1 ,int(path_nested)):
            try:
                url_category = super().get_queryset().get(slug=url[i])
                cat = 'category_' + str(i)
                category_dict[cat] = {}
                category_dict[cat]['title'] = url_category.title
                category_dict[cat]['full_slug'] = category_dict['category']['full_slug'] + url_category.full_slug + '/'
            except:
                pass

        return category_dict
    
    def get_breadcrumbs_ser(self, **kwargs):
        url = self.request.get_full_path()[1:-1].split('/')
        path_nested = len(url)

        category_path = 'product/breadcrumbs/_' + str(path_nested) + '.html'
        category_dict = {
            'category_path': category_path,
            'category': {
                'title': 'Каталог',
                'full_slug': '/category/',
            },
        }

        for i in range(1 ,int(path_nested)):
            try:
                url_category = ''
                if i == (path_nested - 1):
                    url_category = Series.objects.get(slug=url[i])
                else:
                    url_category = Categories.objects.get(slug=url[i])
                cat = 'category_' + str(i)
                category_dict[cat] = {}
                category_dict[cat]['title'] = url_category.title
                category_dict[cat]['full_slug'] = category_dict['category']['full_slug'] + url_category.full_slug + '/'
            except:
                pass

        return category_dict
        
    def get_meta_product(self, **kwargs):
        context = kwargs
        page = self.get_category()

        context['title'] = page.title
        context['description'] = page.description
        context['meta_title'] = page.meta_title or page.title
        context['meta_description'] = page.meta_description or page.title
        context['meta_keywords'] = page.meta_keywords or page.title

        return context