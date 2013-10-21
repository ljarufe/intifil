# -*- coding: utf-8 -*-
""" teams' admin """

from django.contrib import admin
from common.admin import BasePermissionAdmin#, BasePermissionTabularAdmin
from .models import Team, TeamMember, Item


class TeamMemberInline(admin.TabularInline):
    """ TeamMember inline model admin """
    model = TeamMember
    extra = 1
    max_num = 6


class TeamAdmin(BasePermissionAdmin):
    """ Team model admin """
    list_display = ('__unicode__', 'order')
    list_editable = ('order', )
    inlines = [ TeamMemberInline ]


class ItemAdmin(BasePermissionAdmin):
    """ Item model admin """
    list_display = ('__unicode__', 'category', 'order')
    list_editable = ('order', )
    list_display_links = ('__unicode__', 'category')


admin.site.register(Team, TeamAdmin)
admin.site.register(Item, ItemAdmin)
