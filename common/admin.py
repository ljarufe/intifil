# -*- coding: utf-8 -*-

from django.contrib import admin


class BasePermissionAdmin(admin.ModelAdmin):
    """
    Clase base para agregar seguridad
    """
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        """
        Removing delete action from action list
        """
        actions = super(BasePermissionAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']

        return actions


class BasePermissionTabularAdmin(admin.TabularInline):
    """
    Clase base para agregar seguridad
    """
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        """
        Removing delete action from action list
        """
        actions = super(BasePermissionTabularAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']

        return actions