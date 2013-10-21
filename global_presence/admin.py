# -*- coding: utf-8 -*-
""" global_precence's admin """

from django.contrib import admin
from common.admin import BasePermissionAdmin, BasePermissionTabularAdmin
from .models import Item, Country, Team
from .forms import ItemAdminForm


class CountryInline(BasePermissionTabularAdmin):
    """ Country inline model admin """
    model = Country


class ItemAdmin(BasePermissionAdmin):
    """ Item model admin """
    list_display = ('__unicode__', 'team_name', 'category', 'order')
    list_display_links = ('__unicode__', 'team_name', 'category')
    list_editable = ('order', )
    form = ItemAdminForm
    inlines = [ CountryInline ]


class TeamAdmin(BasePermissionAdmin):
    """ Team model admin """
    # changing order of the fields
    fields = (
            'name', 'address_line_1', 'address_line_2','address_line_3',
            'address_line_4', 'phone', 'email', 'image', 'country'
    )
    # for some reason the change of the order on the form is not working
    # maybe due to the tool used to show the django admin
    # form = TeamAdminForm
    list_display = ('__unicode__', 'country')
    list_display_links = list_display


admin.site.register(Item, ItemAdmin)
admin.site.register(Team, TeamAdmin)
