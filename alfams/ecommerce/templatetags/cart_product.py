from django import template
from django.db import transaction
from product.models import Series, Products

register = template.Library()



@register.inclusion_tag('ecommerce/tags/cart-products.html', takes_context=True)
def show_cart_products(context, *args, **kwargs):
    products = args[0]
    for item in products:
        obj = Products.objects.get(pk=item['id'])
        item['obj'] = obj
        item['price'] = get_price(obj)
        print(get_price(obj))
    print(products)
        
    return {'products': products}


def get_price(obj):
    from ecommerce.models import Course
    course = Course.objects.filter(parent_brand=obj.product_brand).filter(parent_series=obj.parent)[0]

    real = obj.product_price - (obj.product_price / 100 * course.discount_real)
    real = real + (real / 100 * course.extra_charge)
    real = round(real)

    fake = 100 - course.discount_fake
    fake = real / fake * 100
    fake = round(fake)
    return {'real': real, 'fake': fake, 'discount': course.discount_fake}