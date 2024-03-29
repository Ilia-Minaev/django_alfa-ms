from django import template
from product.models import Categories
register = template.Library()


class Menu():
    categories = None

    @register.inclusion_tag('product/tags/top-menu.html')
    def show_top_menu():
        #categories = get_tree()
        categories = Menu.get_tree()
        return {'categories': categories}
            

    @register.inclusion_tag('product/tags/sidebar-menu.html')
    def show_sidebar_menu():
        categories = Menu.get_tree()
        return {'categories_sidebar': categories}
    
    @register.inclusion_tag('website/tags/sitemap.html')
    def get_sitemap():
        from website.models import Pages, SubPages
        menu_items = Pages.objects.filter(is_published=True).values('id', 'title', 'slug')
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
                item['childs'] = sub_items[item['id']]

        categories = Menu.get_tree()
        return {'pages': menu_items, 'categories': categories}

    def get_tree():
        if Menu.categories:
            return Menu.categories
        
        categories = Categories.objects.filter(is_published=True).values('id', 'title', 'image', 'icon', 'level', 'parent_id', 'full_slug')
        max_level = list()
        category_dict = dict()

        #максимальный левел категории
        for item in categories:
            max_level.append(item['level'])
        max_level = max(max_level)

        #распределяем категории в словарь, где ключ - это левел, значение - список категорий
        for lvl in range(0, max_level + 1):
            category_dict[lvl] = []
            for item in categories:
                if item['level'] == lvl:
                    category_dict[lvl].append(item)

        #перебираем словарь, начиная с последнего ключа, и перетаскиваем категории из списка в словарь на уровень ниже
        for lvl in range(max_level, -1, -1):
            for item in category_dict[lvl]:
                if item['parent_id']:
                    for cat in category_dict[lvl - 1]:
                        if item['parent_id'] == cat['id']:
                            if cat.get('childs'):
                                cat['childs'].append(item)
                            else:
                                cat['childs'] = []
                                cat['childs'].append(item)
                                
        Menu.categories = category_dict[0]
        return category_dict[0]