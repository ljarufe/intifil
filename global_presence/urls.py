# -*- coding: utf-8 -*-
""" global presence's urls """

from django.conf.urls import patterns, url

from .views import ItemDetail, CountryDetail

urlpatterns = patterns(
    'global_presence.views',
    url('^get_mini_by_screen/$',
        'json_get_mini_by_screen',
        name='global_presence.get_mini_by_screen'
    ),
    url('^get_team_by_screen/$',
        'json_get_team_by_screen',
        name='global_presence.get_team_by_screen'
    ),    
    url(r'^(?P<slug>[-_\w]+)/$',
        ItemDetail.as_view(),
        name='global_presence.itemdetailview'),
    url(r'^(?P<item_slug>[-_\w]+)/(?P<slug>[-_\w]+)/$',
        CountryDetail.as_view(),
        name='global_presence.subitemdetailview'),        
)
