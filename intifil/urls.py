# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    # media and static
    (r'^media/(?P<path>.*)$','django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT,'show_indexes': True}),
    (r'^static/(?P<path>.*)$','django.views.static.serve',
         {'document_root': settings.STATIC_ROOT,'show_indexes': True}),
    # third apps
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # local apps
    url(r'^sitemap/$', include('sitemap.urls')),
    url(r'^global_presence/', include('global_presence.urls')),
    url(r'^teams/', include('teams.urls')),
    url(r'^', include('items.urls')),
)
