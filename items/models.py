# -*- coding: utf-8 -*-
""" items' models """

from itertools import chain

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.conf import settings

from easy_thumbnails.fields import ThumbnailerImageField
from embed_video.base import detect_backend
from embed_video.fields import EmbedVideoField
from tinymce.models import HTMLField
from autoslug.fields import AutoSlugField

from common.utils import highlyRandomName
from items.constants import HOME_PHOTO_CHOICES


class Category(models.Model):
    """
    Categoría de los items
    """
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True,
                         max_length=255, always_update=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ("id",)

    def __unicode__(self):
        return u"{obj.name}".format(obj=self)

    def get_absolute_url(self):
        return reverse('home', args=(self.slug,))

    @property
    def all_item_set(self):
        """
        returns an ordered list with:
        * items.item
        * global_presence.item
        * teams.item
        related to this category
        """
        items = list(
            chain(self.item_set.all(), self.global_presence_item_set.all(),
                  self.teams_item_set.all())
        )
        return sorted(items, key=lambda item: item.order)

    @property
    def all_home_item_set(self):
        """
        returns an ordered list with:
        * items.item
        * global_presence.item
        * teams.item
        related to this category that have a home photo
        """
        home_filter = dict(home_photo__isnull=False)
        items = list(
            chain(
                self.item_set.filter(**home_filter),
                self.global_presence_item_set.filter(**home_filter),
                self.teams_item_set.filter(**home_filter)
            )
        )
        return sorted(items, key=lambda item: item.order)


class HomePhoto(models.Model):
    """
    Foto para la pantalla de inicio
    """
    def get_photo_path(self, filename):
        return u'photos/%s' % highlyRandomName(filename)

    shape = models.CharField(max_length=1, choices=HOME_PHOTO_CHOICES)
    image = ThumbnailerImageField(upload_to=get_photo_path)

    class Meta:
        verbose_name = "home photo"
        verbose_name_plural = "home photos"    

    def __unicode__(self):
        return u"{id} [{shape}]".format(shape=self.get_shape_display(),
                                        id=self.id)

    def get_item(self):
        """
        Devuelve el item relacionado a la foto
        """
        item = None
        if hasattr(self, 'item'):
            item = self.item
        elif hasattr(self, 'teams_item_set'):
            item  = self.teams_item_set
        elif hasattr(self, 'global_presence_item_set'):
            item = self.global_presence_item_set
        return item
    get_item.allow_tags = True


class ItemHomeManager(models.Manager):
    def get_query_set(self):
        return super(ItemHomeManager, self).get_query_set().filter(
            home_photo__isnull=False)


class Item(models.Model):
    """
    Item de la página
    """
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    category = models.ForeignKey(Category)
    home_photo = models.OneToOneField(HomePhoto, null=True, blank=True)
    slug = AutoSlugField(populate_from='name', unique=True,
                         max_length=255, always_update=True)
    show_sub_pages_on_sitemap = models.BooleanField(default=False)

    # managers
    objects = models.Manager()
    home_objects = ItemHomeManager()

    class Meta:
        ordering = ("order",)
        get_latest_by = ("order",)

    def __unicode__(self):
        return u"{obj.name}".format(obj=self)

    @classmethod
    def set_order(cls, id_item, order):
        obj = cls.objects.get(id=id_item)
        obj.order = order
        obj.save()

    @classmethod
    def get_default_order(cls):
        return cls.home_objects.latest().order + 1

    def get_absolute_url(self):
        return reverse(
            'item_detail',
            kwargs={'slug': self.slug, 'slug_category': self.category.slug}
        )

    def get_thumbnail_by_screen(self, screen):
        """
        Devuelve el thumbnail según la resolución y al forma de la foto
        """
        return self.home_photo.image[
            "{screen}_{shape}".format(screen=screen,
                                      shape=self.home_photo.get_shape_display())
        ].url

    def get_mini_by_screen(self, screen):
        """
        Devuelve el thumbnail según la resolución y al forma de la foto para la
        galería
        """
        return self.home_photo.image["mini_{screen}".format(screen=screen)].url

    @property
    def get_sub_pages(self):
        """ returns the subpages of this item """
        return self.subitem_set.all()    


class SubItem(models.Model):
    """
    Subitems en la página de detalles del item
    """
    name = models.CharField(max_length=100)
    description = HTMLField(blank=True)
    item = models.ForeignKey(Item)
    slug = AutoSlugField(populate_from='name', unique=True,
                         max_length=255, always_update=True)    
    order = models.PositiveSmallIntegerField(null=True, blank=True, default=0)

    class Meta:
        ordering = ("order",)
        unique_together = ("item", "order",)

    def __unicode__(self):
        return u"{obj.name}".format(obj=self)

    def get_photo_slider(self, screen):
        """
        Devuelve las fotos del item según la resolución
        """
        return [{"thumb": photo.image["slider_{screen}".format(screen=screen)].url,
                 "name": photo.name} for photo in self.photo_set.all()]

    def get_videos(self, screen):
        """
        Devuelve videos en formato embebido
        """
        return [{"video": video.get_embed(screen),
                 "name": video.name} for video in self.video_set.all()]

    def get_absolute_url(self):
        return self.item.get_absolute_url()


class Photo(models.Model):
    """
    Foto de uno de los items
    """
    def get_photo_path(self, filename):
        return u'photos/%s' % highlyRandomName(filename)

    name = models.CharField(max_length=50)
    image = ThumbnailerImageField(upload_to=get_photo_path)
    order = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    subitem = models.ForeignKey(SubItem, null=True)

    class Meta:
        ordering = ['order']
        unique_together = ("order", "subitem",)

    def __unicode__(self):
        return u"{obj.name}".format(obj=self)


class Video(models.Model):
    """
    Video de uno de los items
    """
    name = models.CharField(max_length=50)
    url = EmbedVideoField()
    order = models.IntegerField(null=True, blank=True, default=0)
    subitem = models.ForeignKey(SubItem, null=True)

    class Meta:
        ordering = ['order']    

    def __unicode__(self):
        return u"{obj.name}".format(obj=self)

    def get_embed(self, screen):
        """
        Devuelve el iframe para un video
        """
        size = settings.VIDEO_SIZES[screen]
        backend = detect_backend(self.url)

        return mark_safe(
            '<iframe width="{width}" height="{height}" '
            'src="{url}" frameborder="0" allowfullscreen>'
            '</iframe>'.format(width=size["width"], height=size["height"],
                               url=backend.url)
        )
