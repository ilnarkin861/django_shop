from .models import MenuItems


def get_main_menu(request):
    context = {}
    context['main_menu'] = MenuItems.objects.filter(menu__menu_id = 'main_menu', is_show = True)
    return context

