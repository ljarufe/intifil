# -*- coding: utf-8 -*-

from modeltranslation.translator import translator, TranslationOptions
from items.models import Category, Item, SubItem, Photo, Video


class CategoryTranslation(TranslationOptions):
    """
    Translation options for Cateogry model
    """
    fields = ("name",)


class ItemTranslation(TranslationOptions):
    """
    Translation options for Item model
    """
    fields = ("name",)


class SubItemTranslation(TranslationOptions):
    """
    Translation options for SubItem model
    """
    fields = ("name", "description",)


class MediaTranslation(TranslationOptions):
    """
    Translation options for photo and video model
    """
    fields = ("name",)


translator.register(Category, CategoryTranslation)
translator.register(Item, ItemTranslation)
translator.register(SubItem, SubItemTranslation)
translator.register(Photo, MediaTranslation)
translator.register(Video, MediaTranslation)