from django import template
from product.models import Series, Products
from ecommerce.utils import get_products_by_order
register = template.Library()



@register.inclusion_tag('ecommerce/tags/cart-products.html', takes_context=True)
def show_cart_products(context, *args, **kwargs):
    products = get_products_by_order(args[0])
    #course = get_products_by_order(session=args[0])
    #print(course)
    return {'products': products}


#def get_products_by_order(session):
#    products = session
#    for item in products:
#        obj = Products.objects.get(pk=item['id'])
#        item['obj'] = obj
#        item['price'] = get_price(obj)
        
#    return products


#def get_price(obj):
#    from ecommerce.models import Course
#    course = Course.objects.filter(parent_brand=obj.product_brand).filter(parent_series=obj.parent)[0]
#
#    real = obj.product_price - (obj.product_price / 100 * course.discount_real)
#    real = real + (real / 100 * course.extra_charge)
#    real = round(real)
#
#    fake = 100 - course.discount_fake
#    fake = real / fake * 100
#    fake = round(fake)
#
#    return {'real': real, 'fake': fake, 'discount': course.discount_fake}