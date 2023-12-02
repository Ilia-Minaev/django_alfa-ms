from django import template
from django.db import transaction

register = template.Library()


@register.inclusion_tag('product/tags/tabs-colors.html', takes_context=True)
def show_tabs(context, *args, **kwargs):
    tabs = args[0]
    tabs_nav = set()

    for item in tabs:
        with transaction.atomic():
            tabs_nav.add(item.parent)
        
    return {'tabs_nav': tabs_nav, 'tabs_items': tabs}

@register.inclusion_tag('product/tags/products.html', takes_context=True)
def show_products(context, *args, **kwargs):
    products = args[0]
    products_color = []
    #print()

    for item in products:
        code = item.product_code.split('_')[0]
        products_color.append(code)


    products_color = list(set(products_color))
        
    return {'products': products, 'products_color': products_color}