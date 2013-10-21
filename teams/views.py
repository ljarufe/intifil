# -*- coding: utf-8 -*-
""" teams' views """

from django.views.generic import DetailView

from common.utils import json_response
from teams.models import Team, TeamMember


class TeamDetailView(DetailView):
    """
    Galería de un item
    """
    model = Team
    template_name = "teams/team_detail.html"


def json_get_mini_by_screen(request):
    """
    :return: devuelve las fotos de los items según la resolución para las
    miniaturas de la galería
    """
    team = Team.objects.latest('id')
    if team:
        queryset = team.item.category.all_item_set
    else:
        queryset = []
    screen = request.GET["screen"]
    data = [{"name": item.name,
             "thumb": item.get_mini_by_screen(screen),
             "slug": item.slug,
             "url": item.get_absolute_url()} for item in queryset]

    return json_response(data)


def json_get_photo_by_screen(request, slug):
    """
    devuelve las foto del equipo según la resolución
    """
    screen = request.GET["screen"]
    item = Team.objects.get(slug=slug)
    data = {"name": item.name, "thumb": item.get_photo_by_screen(screen)}

    return json_response(data)


def json_get_teammember_photos_by_screen(request):
    """
    returns the teammember photos based on the resolution
    """
    screen = request.GET["screen"]
    data = []
    for pos, item in enumerate(TeamMember.objects.all()):
        data.append({"thumb": item.get_photo_by_screen(screen, pos)})

    return json_response(data)
