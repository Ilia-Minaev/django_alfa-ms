from django import template

from website.models import Pages, SubPages
from blog.models import Articles, Portfolio

register = template.Library()


@register.inclusion_tag('website/tags/header_menu.html', takes_context=False)
def show_header_menu(*args, **kwargs):
    menu_items = Pages.objects.filter(is_published=True).filter(is_header=True).values('id', 'title', 'slug')

    sub_pages = SubPages.objects.filter(is_published=True).values('id', 'title', 'slug', 'parent_id')
    sub_items = {}

    for item in sub_pages:
        if sub_items.get(item['parent_id']):
            sub_items[item['parent_id']].append(item)
        else:
            sub_items[item['parent_id']] = []
            sub_items[item['parent_id']].append(item)

    for item in menu_items:
        if sub_items.get(item['id']):
            item['childrens'] = sub_items[item['id']]

    article_last = Articles.objects.last()
    portfolio_last = Portfolio.objects.last()
    
    return {"menu_items": menu_items, 'article_last': article_last, 'portfolio_last': portfolio_last}

@register.inclusion_tag('website/tags/footer_menu.html', takes_context=False)
def show_footer_menu(*args, **kwargs):
    menu_items = Pages.objects.filter(is_published=True).filter(is_footer=True)
    return {"menu_items": menu_items,}