# -*- coding: utf-8 -*-

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from common.admin import BasePermissionAdmin
from items.models import Category, Photo, HomePhoto, Item, Video, SubItem


class CategoryAdmin(BasePermissionAdmin, TranslationAdmin):
    """
    Category model admin
    """
    list_display = ("name", "slug",)


class PhotoInLine(admin.TabularInline):
    """
    Photo inline model admin
    """
    model = Photo
    exclude = ("name",)


class VideoInLine(admin.TabularInline):
    """
    Video inline model admin
    """
    model = Video
    exclude = ("name",)


class HomePhotoAdmin(admin.ModelAdmin):
    """
    Home photo model admin
    """
    list_display = ("get_item", "get_shape_display",)


class ItemAdmin(TranslationAdmin):
    """
    Item model admin
    """
    list_display = ("name", "category", "order",)
    list_display_links = ("name", "category")
    list_editable = ('order', )
    list_filter = ("category",)
    exclude = ('order',)

    def save_model(self, request, obj, form, change):
        """
        Guarda un nuevo item de la página de inicio con el orden por defecto
        al final de la lista
        """
        if not change:
            if form.cleaned_data["home_photo"]:
                obj.order = Item.get_default_order()
        obj.save()


class SubItemAdmin(TranslationAdmin):
    """
    Subitem model admin
    """
    list_display = ("name", "item", "order",)
    list_display_links = ("name", "item")
    list_editable = ('order', )    
    list_filter = ("item",)
    inlines = [PhotoInLine, VideoInLine,]


class PhotoVideoAdmin(TranslationAdmin):
    """
    Photo and video model admin
    """
    list_display = ("name", "subitem", "order",)
    list_display_links = ("name", "subitem")
    list_editable = ('order', )
    list_filter = ("subitem",)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Photo, PhotoVideoAdmin)
admin.site.register(HomePhoto, HomePhotoAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(SubItem, SubItemAdmin)
admin.site.register(Video, PhotoVideoAdmin)
