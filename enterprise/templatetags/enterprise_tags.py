# -*- coding: utf-8 -*-

from django import template
from ..models import Enterprise

register = template.Library()

@register.assignment_tag
def get_enterprise():
    """
    Retorna una variable con el último objeto enterprise
    """
    try:
        return Enterprise.objects.latest()
    except Enterprise.DoesNotExist:
        return None