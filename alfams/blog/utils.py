from gallery.models import Name, Images

class PostMixin():

    obj = None


    def get_post(self, **kwargs):
        self.obj = super().get_queryset().get(slug=self.kwargs['post_slug'])
        return self.obj
    
    def get_gallery(self, **kwargs):
        post_id = self.obj.gallery_id
        try:
            gallery_name = Name.objects.get(pk=post_id, is_published=True).pk
            gallery_image = Images.objects.filter(parent_id=gallery_name).filter(is_published=True)
            return gallery_image
        except:
            return False
    
    def get_meta_post_single(self, **kwargs):
        context = kwargs
        page = self.obj

        context['title'] = page.title
        context['description'] = page.description
        context['meta_title'] = page.meta_title or page.title
        context['meta_description'] = page.meta_description or page.title
        context['meta_keywords'] = page.meta_keywords or page.title

        return context
    
    def get_next_object(self, *args, **kwargs):
        try:
            next_object = super().get_queryset().filter(is_published=True).filter(date_created__gt=args[0]).order_by('date_created').first()
        except:
            next_object = False

        return next_object
    
    def get_previous_object(self, *args, **kwargs):
        try:
            previous_object = super().get_queryset().filter(is_published=True).filter(date_created__lt=args[0]).order_by('-date_created').first()
        except:
            previous_object = False

        return previous_object