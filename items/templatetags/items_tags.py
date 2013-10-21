# -*- coding: utf-8 -*-

from django import template
from items.models import Category

register = template.Library()


@register.inclusion_tag('items/templatetags/menu.html')
def get_menu():
    """
    Devuelve el menú de categorías
    """
    return {'categories': Category.objects.all()}


@register.filter('next_in_loop')
def next_in_loop(value, arg):
    """
    Devuelve el siguiente elemento en
    """
    index = (int(arg) + 1) % len(value)

    return {"index": index+1, "item": value[index]}
