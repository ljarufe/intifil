# -*- coding: utf-8 -*-
""" teams' models """

from django.db import models
from django.core.urlresolvers import reverse

from autoslug.fields import AutoSlugField
from common.utils import highlyRandomName
from easy_thumbnails.fields import ThumbnailerImageField
from items.models import ItemHomeManager
from tinymce.models import HTMLField


class Item(models.Model):
    """ Stores information of each item on this application """
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True,
                         max_length=255, always_update=True)
    category = models.ForeignKey('items.Category',
                                 related_name='teams_item_set',
                                 blank=True, null=True)
    home_photo = models.OneToOneField('items.HomePhoto', null=True, blank=True,
                                      related_name='teams_item_set')
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
        """  """
        team_set = self.team_set.all()
        if team_set:
            return team_set[0].get_absolute_url()
        return reverse('home')

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
        Si tiene algun team (solo deberia existir 1) retorna su thumbnail
        sino retorna el thumbnail del item
        """
        team = self.team_set.latest('id')
        if team:
            thumb = team.get_mini_by_screen(screen)
        else:
            thumb = self.home_photo.image[
                "mini_{screen}".format(screen=screen)].url
        return thumb

    @property
    def get_sub_pages(self):
        """ returns the subpages of this item """
        return self.team_set.all()


class Team(models.Model):
    """
    Equipo de trabajo
    """
    def get_photo_path(self, filename):
        return u'photos/%s' % highlyRandomName(filename)

    name = models.CharField(max_length=200)
    description = HTMLField(blank=True)
    mini_photo = ThumbnailerImageField(upload_to=get_photo_path, null=True)
    photo = ThumbnailerImageField(upload_to=get_photo_path, null=True)
    slug = AutoSlugField(populate_from='name', unique=True,
                         max_length=255, always_update=True)
    order = models.IntegerField(default=0)
    item = models.ForeignKey(Item)

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return u"{obj.name}".format(obj=self)

    def get_absolute_url(self):
        return reverse('team_detail', args=[self.slug])

    def get_mini_by_screen(self, screen):
        """
        Devuelve el thumbnail según la resolución y al forma de la foto para la
        galería
        """
        return self.mini_photo["mini_{screen}".format(screen=screen)].url

    def get_photo_by_screen(self, screen):
        """
        Devuelve la foto según la resolución y al forma de la foto para la
        galería
        """
        return self.photo[
            "teams_team_photo_{screen}".format(screen=screen)].url


class TeamMember(models.Model):
    """
    Miembro del equipo
    """
    def get_photo_path(self, filename):
        return u'photos/%s' % highlyRandomName(filename)

    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    photo = ThumbnailerImageField(upload_to=get_photo_path, null=True)
    team = models.ForeignKey(Team)

    def __unicode__(self):
        return u"{obj.name}".format(obj=self)

    class Meta:
        verbose_name = "team member"
        verbose_name_plural = "team members"
        ordering = ['id']

    def get_photo_by_screen(self, screen, position):
        """ Devuelve la foto según la resolución """
        return self.photo[
            "teams_teammember_photo_{position}_{screen}".format(
                position=position, screen=screen)].url
