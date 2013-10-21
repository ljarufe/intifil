# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from teams.views import TeamDetailView

urlpatterns = patterns('teams.views',
    url(
        regex=r'^get_mini_by_screen/$',
        view='json_get_mini_by_screen',
        name='get_teammini_by_screen'
    ),
    url(
        regex=r'^get_photo_by_screen/(?P<slug>[-_\w]+)/$',
        view='json_get_photo_by_screen',
        name='get_teamphoto_by_screen'
    ),
    url(
        regex=r'^get_teammember_photos_by_screen/$',
        view='json_get_teammember_photos_by_screen',
        name='get_teammember_photos_by_screen'
    ),
    url(
        regex=r'^(?P<slug>[-_\w]+)/$',
        view=TeamDetailView.as_view(),
        name="team_detail"
    ),
)
