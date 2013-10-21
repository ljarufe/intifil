# -*- coding: utf-8 -*-
""" global_presence's views """

from django.views.generic import DetailView
from django.shortcuts import get_object_or_404

from common.utils import json_response
from .models import Item, Country, Team

from itertools import chain


class BaseContextDataMixin(object):
    """ defines common the context data for each view """

    def add_context_data(self, context, item=True, countries=True,
                         selected=None, teams=False):
        """
        adds the following data to the context:
        * Item
        * Related Countries
        * selected variable // it should be the slug of the object
        * all Team objects
        """
        # adding subitten
        if item:
            try:
                context['item'] = Item.objects.get(id=1)
            except (Item.DoesNotExist):
                context['item'] = None
        # adding related countries
        if countries:
            try:
                context['countries'] = Country.objects.all()
            except (Country.DoesNotExist):
                context['countries'] = None
        # adding selected variable
        if selected:
            context['selected'] = selected
        # adding team objects
        if teams:
            context['teams'] = Team.objects.all()
        return context


class ItemDetail(BaseContextDataMixin, DetailView):
    """ shows the item detail page """
    model = Item
    template_name = 'global_presence/index.html'

    def get_context_data(self, **kwargs):
        """ adds some data do the context """
        context = super(self.__class__, self).get_context_data(**kwargs)
        return self.add_context_data(
            context, selected=context['object'].slug, teams=True
        )
    

class CountryDetail(BaseContextDataMixin, DetailView):
    """ shows the subitem detail page """
    model = Country
    template_name = 'global_presence/detail_1.html'

    def get(self, request, *args, **kwargs):
        """
        verifies that the category slug exist before processing the get request
        """
        get_object_or_404(Item, slug=kwargs.get('item_slug'))
        self.team_id = request.GET.get('team')
        return super(self.__class__, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """ adds some data do the context """
        context = super(self.__class__, self).get_context_data(**kwargs)
        # teams from the country
        context['team_set'] = context['object'].team_set.all()
        # position of the team in the team set
        try:
            context['go_to_page'] = list(
                context['team_set'].values_list('id', flat=True)
            ).index(int(self.team_id))
        except (ValueError, TypeError):
            pass
        return self.add_context_data(context, selected=context['object'].slug)


def json_get_mini_by_screen(request):
    """ returns flags thumbnails based on the creen resolution """
    screen = request.GET["screen"]
    qs = tuple(chain(Item.objects.all(), Country.objects.all()))
    data = [{"id": obj.id,
             "name": obj.name,
             "thumb": obj.get_flag_mini_by_screen(screen),
             "url": obj.get_absolute_url()} for obj in qs]

    return json_response(data)


def json_get_team_by_screen(request):
    """ returns team thumbnails based on the creen resolution """
    screen = request.GET["screen"]
    try:
        country = Country.objects.get(id=int(request.GET["country"]))
    except Country.DoesNotExist:
        data = []
    else:
        qs = country.team_set.all()
        data = [{"id": obj.id,
                 "name": obj.name,
                 "thumb": obj.get_mini_by_screen(screen)} for obj in qs]

    return json_response(data)
