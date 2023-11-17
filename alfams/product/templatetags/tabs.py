from django import template
register = template.Library()


@register.inclusion_tag('product/tags/tabs-colors.html', takes_context=True)
def show_tabs(context, *args, **kwargs):
    tabs = args[0]
    tabs_nav = set()
    from django.db import transaction

    for item in tabs:
        with transaction.atomic():
            parent = item.parent
            tabs_nav.add(parent)
        
    return {'tabs_nav': tabs_nav, 'tabs_items': tabs}