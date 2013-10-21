# -*- coding: utf-8 -*-
""" sitemap's views """

from django.views.generic import ListView

from .models import Column


class SiteMapView(ListView):
    """ shows the site map page """
    model = Column
    template_name = 'sitemap/index.html'
