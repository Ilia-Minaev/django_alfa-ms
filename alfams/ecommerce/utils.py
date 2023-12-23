from product.models import Categories, Series, Products


def get_table_by_order(session):
    products = session
    price_list_real = []
    price_list_fake = []
    
    html_table = ('''
    <table class="table table-borderless table-striped table-hover">
        <thead>
            <tr>
                <th scope="col">Наименование</th>
                <th scope="col">Количество</th>
                <th scope="col">Цена с НДС</th>
                <th scope="col">Скидка</th>
                <th scope="col">Цена с учетом скидки</th>
                <th scope="col">Итого</th>
            </tr>
        </thead>
        <tbody>
    ''')

    for item in products:
        obj = Products.objects.get(pk=item['id'])
        price = get_price(obj)

        qty = item['qty']
        url = obj.get_full_url()
        real = price['real']
        fake = price['fake']
        total_real = qty * real
        total_fake = qty * fake
        discount = price['discount']

        html_table += f'<tr>'
        html_table += f'<td><a href="{url}">{obj.title}</a></td>'
        html_table += f'<td>{qty}</td>'
        html_table += f'<td>{discount}</td>'
        html_table += f'<td>{real}</td>'
        html_table += f'<td>{fake}</td>'
        html_table += f'<td>{total_real}</td>'
        html_table += f'</tr>'

        price_list_real.append(total_real)
        price_list_fake.append(total_fake)

    price_list_real = sum(price_list_real)
    price_list_fake = sum(price_list_fake) - price_list_real

    html_table += '<tr>'
    html_table += f'<td colspan="5" style="text-align: end;"><b>Итого с НДС:</b></td>'
    html_table += f'<td>{price_list_real}</td>'
    html_table += '</tr>'

    html_table += '<tr>'
    html_table += f'<td colspan="5" style="text-align: end;"><b>Сумма скидки:</b></td>'
    html_table += f'<td>{price_list_fake}</td>'
    html_table += '</tr>'

    html_table += ('''
        </tbody>
    </table>
    ''')


    return html_table

def get_products_by_order(session):
    products = session
    for item in products:
        obj = Products.objects.get(pk=item['id'])
        item['obj'] = obj
        item['price'] = get_price(obj)
        
    return products


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