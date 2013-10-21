# -*- coding: utf-8 -*-
""" items' urls """

from django.conf.urls import patterns, url
from .views import HomeView, HomeCategoryView, ItemDetailView,\
    ItemOrderView


urlpatterns = patterns('items.views',
    url(
        regex=r'^items/reorder_home_items/$',
        view=ItemOrderView.as_view(),
        name='reorder_home_items'
    ),
    url(
        regex=r'^items/get_photos_by_screen/$',
        view='json_get_photos_by_screen',
        name='get_photos_by_screen'
    ),
    url(
        regex=r'^items/get_mini_by_screen/$',
        view='json_get_mini_by_screen',
        name='get_mini_by_screen'
    ),
    url(
        regex=r'^items/get_slider_by_screen/$',
        view='json_get_slider_by_screen',
        name='get_slider_by_screen'
    ),
    url(
        regex=r'^(?P<slug_category>[-_\w]+)/(?P<slug>[-_\w]+)/$',
        view=ItemDetailView.as_view(),
        name="item_detail"
    ),
    url(
        regex=r'^(?P<slug>[-_\w]+)/$',
        view=HomeCategoryView.as_view(),
        name="home"
    ),
    url(
        regex=r'^$',
        view=HomeView.as_view(),
        name="home"
    ),
)
