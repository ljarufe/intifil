# -*- coding: utf-8 -*-
""" sitemap's urls """

from django.conf.urls import patterns, url

from .views import SiteMapView


urlpatterns = patterns(
    '',
    url(r'^$', SiteMapView.as_view(), name='sitemap.index'),
)
