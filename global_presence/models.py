# -*- coding: utf-8 -*-
""" global presence's models """

from django.db import models
from django.core.urlresolvers import reverse

from autoslug.fields import AutoSlugField
from easy_thumbnails.fields import ThumbnailerImageField
from common.utils import highlyRandomName
from items.models import ItemHomeManager


def get_photo_path(self, filename):
    return u'photos/%s' % highlyRandomName(filename)


class BaseData(models.Model):
    """ abstract class with all the base data for Item and SubItem classes """  
    # probably we'll need to store the coordinates to make it work dinamically
    # however We'll do it only if we have free time
    # maybe this is not a good idea cause the coordinates could change a little
    # bit between the different browsers
    # anyway this module is amining to be kind of static, (Chris said this) 
    name = models.CharField(max_length=255)
    # the address must be splitted on 3 or lines cause the template requires it
    address_line_1 = models.CharField(max_length=60)
    address_line_2 = models.CharField(max_length=60)
    address_line_3 = models.CharField(max_length=60)
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    class Meta:
        abstract = True        


class Item(BaseData):
    """ Stores the information of each item on this module """
    team_name = models.CharField(max_length=255)    
    fax = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)
    slug = AutoSlugField(populate_from='team_name', unique=True,
                         max_length=255, always_update=True)
    category = models.ForeignKey(
        'items.Category', related_name='global_presence_item_set',
        blank=True, null=True
    )
    home_photo = models.OneToOneField('items.HomePhoto', null=True, blank=True,
                                      related_name='global_presence_item_set')
    description = models.TextField()
    flag_image = ThumbnailerImageField(upload_to=get_photo_path)
    show_sub_pages_on_sitemap = models.BooleanField(default=False)
    order = models.SmallIntegerField(default=0)

    # managers
    objects = models.Manager()
    home_objects = ItemHomeManager()

    class Meta:
        ordering = ("order",)
        get_latest_by = ("order",)
    
    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('global_presence.itemdetailview', args=[self.slug])

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

    def get_flag_mini_by_screen(self, screen):
        """ returns the thumbnail relative to the screen resolution """
        return self.flag_image["gp_item_flag_image_{screen}".\
            format(screen=screen)].url

    @property
    def get_sub_pages(self):
        """ returns the subpages of this item """
        return self.country_set.all()


class Country(models.Model):
    """ stores the countries data """
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True,
                         max_length=255, always_update=True)
    flag_image = ThumbnailerImageField(upload_to=get_photo_path)    
    item = models.ForeignKey(Item)
    order = models.SmallIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Countries'
        ordering = ('order', )

    def get_absolute_url(self):
        """ TODO: HERE ALL THE TEAMS MUST BE SHOWN LIKE YARNS PAGE"""
        return reverse(
            'global_presence.subitemdetailview',
            args=[self.item.slug, self.slug]
        )

    def __unicode__(self):
        return u'%s' % self.name

    def get_flag_mini_by_screen(self, screen):
        """ returns the thumbnail relative to the screen resolution """
        return self.flag_image["gp_country_flag_image_{screen}".\
            format(screen=screen)].url


class Team(BaseData):
    """stores the country teams """    
    slug = AutoSlugField(populate_from='name', unique=True,
                         max_length=255, always_update=True)    
    image = ThumbnailerImageField(upload_to=get_photo_path)
    address_line_4 = models.CharField(max_length=60, blank=True)
    country = models.ForeignKey(Country)

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return self.country.get_absolute_url() + '?team={}'.format(self.id)

    def get_mini_by_screen(self, screen):
        """ returns the thumbnail relative to the screen resolution """
        return self.image["gp_team_image_{screen}".\
            format(screen=screen)].url
