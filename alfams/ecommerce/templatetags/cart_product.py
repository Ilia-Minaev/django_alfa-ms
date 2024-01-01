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

