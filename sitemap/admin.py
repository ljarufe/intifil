# -*- coding: utf-8 -*-
""" sitemap's admin """

from django.contrib import admin

from common.admin import BasePermissionAdmin
from .models import Column, ColumnCategory


class ColumnCategory(admin.TabularInline):
    model = ColumnCategory
    extra = 1

class ColumnAdmin(BasePermissionAdmin):
    inlines = (ColumnCategory,)


admin.site.register(Column, ColumnAdmin)
