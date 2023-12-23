from django import template
from django.db import transaction
from product.models import Series, Products

register = template.Library()


@register.inclusion_tag('product/tags/tabs-colors.html', takes_context=True)
def show_tabs_colors(context, *args, **kwargs):
    #tabs_items = args[0]
    #tabs_nav = set()
    
    #item = Series.objects.get(pk=1)

    items = Products.objects.filter(parent=args[0])

    tabs_items = set()
    tabs_nav = set()

    for item in items:
        tabs_items.add(item.product_color)
        tabs_nav.add(item.product_color.parent)
    #print(t_nav)

    #for item in tabs:
    #    with transaction.atomic():
    #        tabs_nav.add(item.parent)
    
    return {'tabs_nav': tabs_nav, 'tabs_items': tabs_items}

@register.inclusion_tag('product/tags/tabs-colors-product.html', takes_context=True)
def show_tabs_colors_product(context, *args, **kwargs):
    tabs_items = args[0]
    tabs_nav = set()

    for item in tabs_items:
        with transaction.atomic():
            tabs_nav.add(item.product_color.parent)
        
    return {'tabs_nav': tabs_nav, 'tabs_items': tabs_items, 'item_active': args[1]}

@register.inclusion_tag('product/tags/products.html', takes_context=True)
def show_products(context, *args, **kwargs):
    products = args[0]
    products_color = []

    for item in products:
        code = item.product_code.split('_')[0]
        products_color.append(code)

    products_color = list(set(products_color))
        
    return {'products': products, 'products_color': products_color, 'series_url': args[1]}