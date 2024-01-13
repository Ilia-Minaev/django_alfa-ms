from django import template
from product.models import Series, Products
from ecommerce.utils import get_products_by_order, get_total_price
register = template.Library()



@register.inclusion_tag('ecommerce/tags/cart-products.html', takes_context=False)
def show_cart_products(*args, **kwargs):
    products = get_products_by_order(args[0])
    total_price = get_total_price(products)
    return {'products': products, 'total_price': total_price}

@register.inclusion_tag('ecommerce/tags/cart-products-print.html', takes_context=False)
def show_cart_products_print(*args, **kwargs):
    products = get_products_by_order(args[0])
    total_price = get_total_price(products)
    return {'products': products, 'total_price': total_price}


@register.inclusion_tag('ecommerce/tags/callback/_modal-callback-btn.html', takes_context=False)
def show_modal_callback_btn(*args, **kwargs):
    pass

@register.inclusion_tag('ecommerce/tags/callback/_modal-callback.html', takes_context=False)
def show_modal_callback(*args, **kwargs):
    return {'url': args[0]}

@register.inclusion_tag('ecommerce/tags/callback/_modal-consultation-btn.html', takes_context=False)
def show_modal_consultation_btn(*args, **kwargs):
    pass

@register.inclusion_tag('ecommerce/tags/callback/_modal-consultation.html', takes_context=False)
def show_modal_consultation(*args, **kwargs):
    return {'url': args[0]}


@register.inclusion_tag('ecommerce/tags/favorites-btn.html', takes_context=False)
def check_favorites(*args, **kwargs):
    return check_favorites_and_comparison(args, 'favorites')

@register.inclusion_tag('ecommerce/tags/comparison-btn.html', takes_context=False)
def check_comparison(*args, **kwargs):
    return check_favorites_and_comparison(args, 'comparison')

def check_favorites_and_comparison(args, key):
    session = args[0].get(key)
    object = args[1]
    model = args[2]

    try:
        url_redirect = args[3]
    except:
        url_redirect = False
    icon = None

    if session:
        for item in session:
            if item['id'] == object.id and item['type'] == model:
                icon = True
                break
            icon = False
    else:
        icon = False

    return {'icon': icon, 'object': object, 'model': model, 'url_redirect': url_redirect}


@register.inclusion_tag('ecommerce/tags/comparison-products.html', takes_context=False)
def show_comparison_products(*args, **kwargs):
    return {'products': args[0], 'from_url': args[1], 'session': args[2],}

@register.inclusion_tag('ecommerce/tags/comparison-series.html', takes_context=False)
def show_comparison_series(*args, **kwargs):
    return {'series': args[0], 'from_url': args[1], 'session': args[2],}