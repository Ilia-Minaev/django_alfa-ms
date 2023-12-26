from product.models import Categories, Series, Products
from django.urls import reverse_lazy

class ProductMixin():

    obj = None

    def get_category(self, **kwargs):
        #print(self.kwargs['slug'])
        if self.obj:
            return self.obj
        else:
            #url = self.request.get_full_path()[1:-1].split('/')[-1]
            url = self.kwargs['slug']
            self.obj = super().get_queryset().get(slug=url)
            return self.obj
        
    def get_meta_product(self, **kwargs):
        context = kwargs
        page = self.get_category()

        context['title'] = page.title
        context['description'] = page.description
        context['meta_title'] = page.meta_title or page.title
        context['meta_description'] = page.meta_description or page.title
        context['meta_keywords'] = page.meta_keywords or page.title

        return context
    

class BreadcrumbsMixin():
    slug_list = None
    category = reverse_lazy('shop:category')
    series = reverse_lazy('shop:series')
    product = reverse_lazy('shop:product')

    def _get_slugs(self, **kwargs):
        url = self.request.get_full_path()[1:-1]
        slug_list = url.split('/')
        self.slug_list = slug_list

        return slug_list

    def _breadcrumbs_start(self, kwargs):
        breadcrumbs_list = [
            {
                'title': 'Главная',
                'full_slug': '/',
            },
            {
                'title': 'Каталог',
                'full_slug': self.category,
            },
        ]
        return breadcrumbs_list

    def _breadcrumbs_category(self, kwargs):
        categories = []
        for item in kwargs:
            try:
                cat = Categories.objects.get(slug=item)
            except:
                pass
            categories.append({
                'title': cat.title,
                'full_slug': self.category + cat.full_slug + '/',
            })

        return categories

    def _breadcrumbs_series(self, kwargs):
        item = Series.objects.get(slug=kwargs)
        return [{
            'title': item.title,
            'full_slug': self.series + item.full_slug + '/',
        }]
    
    def _breadcrumbs_product(self, kwargs):
        item = Products.objects.get(slug=kwargs)
        return [{
            'title': item.title,
            'full_slug': self.product + item.full_slug + '/',
        }]
    

    def breadcrumbs_category(self, **kwargs):
        slug_list = self._get_slugs()

        breadcrumbs_start = self._breadcrumbs_start(kwargs=slug_list)
        breadcrumbs_category = self._breadcrumbs_category(kwargs=slug_list[2:])

        return breadcrumbs_start + breadcrumbs_category

    def breadcrumbs_series(self, **kwargs):
        slug_list = self._get_slugs()

        breadcrumbs_start = self._breadcrumbs_start(kwargs=slug_list)
        breadcrumbs_category = self._breadcrumbs_category(kwargs=slug_list[2:-1])
        breadcrumbs_series = self._breadcrumbs_series(kwargs=slug_list[-1])

        return breadcrumbs_start + breadcrumbs_category + breadcrumbs_series
    
    def breadcrumbs_product(self, **kwargs):
        slug_list = self._get_slugs()
        i = len(slug_list)

        breadcrumbs_start = self._breadcrumbs_start(kwargs=slug_list)
        breadcrumbs_category = self._breadcrumbs_category(kwargs=slug_list[2:i-2])
        breadcrumbs_series = self._breadcrumbs_series(kwargs=slug_list[i-2])
        breadcrumbs_product = self._breadcrumbs_product(kwargs=slug_list[i-1])

        return breadcrumbs_start + breadcrumbs_category + breadcrumbs_series + breadcrumbs_product