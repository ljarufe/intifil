# -*- coding: utf-8 -*-

from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
# from tinymce.models import HTMLField
from common.utils import highlyRandomName


class Enterprise(models.Model):
    """
    Datos de la empresa
    """
    def get_photo_path(self, filename):
        return u'photos/%s' % highlyRandomName(filename)

    name = models.CharField(max_length=30)
    logo = ThumbnailerImageField(upload_to=get_photo_path)
    message = models.TextField(blank=True)

    def __unicode__(self):
        return u"{obj.name}".format(obj=self)

    class Meta:
        get_latest_by = ("id",)
