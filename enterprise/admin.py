# -*- coding: utf-8 -*-

from django.contrib import admin
from common.admin import BasePermissionAdmin
from .models import Enterprise


class EnterpriseAdmin(BasePermissionAdmin):
    """
    Enterprise model admin
    """
    list_display = ("name", "message")
    # list_editable = ("message",)

admin.site.register(Enterprise, EnterpriseAdmin)
