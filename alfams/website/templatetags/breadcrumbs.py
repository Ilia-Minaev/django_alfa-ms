from django import template
#from website.models import Pages
register = template.Library()


@register.inclusion_tag('website/tags/breadcrumbs.html', takes_context=True)
def show_breadcrumbs(context):
    path_items = context.request.get_full_path()
    if path_items == '/':
        return {"path_items": False,}
    path_items = path_items.split('/')

    full_path = ''
    full_path_items = []

    for item in path_items:
        if item:
            full_path += item + '/'
            full_path_items.append(full_path)
    return {"path_items": context,}


## test
@register.inclusion_tag('website/tags/breadcrumbs/_start.html')
def breadcrumb_start():
    pass
@register.inclusion_tag('website/tags/breadcrumbs/_end.html')
def breadcrumb_end():
    pass
 
 
@register.inclusion_tag('website/tags/breadcrumbs/_home.html')
def breadcrumb_home(url='/', title=''):
    return {
        'url': url,
        'title': title
    }
 
 
@register.inclusion_tag('website/tags/breadcrumbs/_item.html')
def breadcrumb_item(url, title, position):
    return {
        'url': url,
        'title': title,
        'position': position
    }
 
 
@register.inclusion_tag('website/tags/breadcrumbs/_active.html')
def breadcrumb_active(url, title, position):
    return {
        'url': url,
        'title': title,
        'position': position
    }