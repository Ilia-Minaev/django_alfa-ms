from django import template
from django.db import transaction
from product.models import Series, Products

register = template.Library()


@register.inclusion_tag('product/tags/tabs-colors.html', takes_context=False)
def show_tabs_colors(*args, **kwargs):
    items = Products.objects.filter(parent=args[0])

    tabs_items = set()
    tabs_nav = set()

    for item in items:
        tabs_items.add(item.product_color)
        tabs_nav.add(item.product_color.parent)
    
    return {'tabs_nav': tabs_nav, 'tabs_items': tabs_items}

@register.inclusion_tag('product/tags/tabs-colors-product.html', takes_context=False)
def show_tabs_colors_product(*args, **kwargs):
    tabs_items = args[0]
    tabs_nav = set()

    for item in tabs_items:
        with transaction.atomic():
            tabs_nav.add(item.product_color.parent)
        
    return {'tabs_nav': tabs_nav, 'tabs_items': tabs_items, 'item_active': args[1]}

@register.inclusion_tag('product/tags/products.html', takes_context=False)
def show_products(*args, **kwargs):
    return {'products': args[0], 'from_url': args[1], 'session': args[2], 'col': args[3]}

@register.inclusion_tag('product/tags/categories.html', takes_context=False)
def show_categories(*args, **kwargs):
    return {'categories': args[0], 'col': args[1]}

