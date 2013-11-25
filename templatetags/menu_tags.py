from django import template
from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu.html')
def show_menu(user=None):
    menuitems = []
    for i in MenuItem.objects.all().order_by("order"):
        if i.visibility == i.ANYONE:
            menuitems.append(i)
        elif i.visibility == i.DISABLED:
            pass
        elif i.visibility == i.ANONYMOUS and user is not None and not user.is_authenticated():
            menuitems.append(i)
        elif i.visibility == i.USERS and user is not None and user.is_authenticated():
            menuitems.append(i)
        elif i.visibility == i.MODERATORS and user is not None and (user.is_staff or user.is_superuser):
            menuitems.append(i)
        elif i.visibility == i.ADMINS and user is not None and user.is_superuser:
            menuitems.append(i)
    return {'menuitems': menuitems}
