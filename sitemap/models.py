# -*- coding: utf-8 -*-
""" sitemap's models """

from django.db import models


class Column(models.Model):
    """ stores the sitemap columns """
    name = models.CharField(max_length=120)
    categories = models.ManyToManyField(
        'items.Category', through='ColumnCategory')
    include_intranet_link = models.BooleanField(default=False)
    include_sitemap_link = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return unicode(self.name)


class ColumnCategory(models.Model):
    """ intermediate model between Column and Category models """
    category = models.ForeignKey('items.Category')
    column = models.ForeignKey(Column)
    order = models.SmallIntegerField(default=0)
