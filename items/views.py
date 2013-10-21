# -*- coding: utf-8 -*-

from itertools import chain

from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, FormView

from common.utils import json_response
from items.forms import OrderForm
from items.models import Item, Category, SubItem


class HomeView(TemplateView):
    """
    Vista de inicio de la página, contiene el collage de imágenes
    """
    template_name = "items/home.html"


class HomeCategoryView(HomeView):
    """
    Vista de inicio de la página, contiene el collage de imágenes para una
    categoría en especial
    """
    def get_context_data(self, **kwargs):
        context = super(HomeCategoryView, self).get_context_data(**kwargs)
        context['category'] = self.kwargs["slug"]

        return context


class ItemDetailView(ListView):
    """
    Galería de un item
    """
    model = SubItem
    template_name = "items/item_detail.html"

    def get_queryset(self):
        return SubItem.objects.filter(item__slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context['item'] = get_object_or_404(Item, slug=self.kwargs["slug"])
        context['category'] = self.kwargs["slug_category"]

        return context


class ItemOrderView(FormView):
    """
    Vista para ordenar items de inicio
    """
    template_name = "items/reorder_home_items.html"
    form_class = OrderForm
    success_url = '/admin/'

    def form_valid(self, form):
        form.reorder_items()

        return super(ItemOrderView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ItemOrderView, self).get_context_data(**kwargs)
        context['items'] = Item.home_objects.all()

        return context


def json_get_photos_by_screen(request):
    """
    devuelve las fotos de los items según la resolución
    """
    screen = request.GET["screen"]
    if request.GET["category"]:
        category = get_object_or_404(Category, slug=request.GET["category"])
        # items = Item.home_objects.filter(category=category)
        items  = category.all_home_item_set
    else:
        # items = Item.home_objects.all()
        from teams.models import Item as teams_item
        from global_presence.models import Item as global_presence_item
        items = list(
            chain(
                Item.home_objects.all(),
                teams_item.home_objects.all(),
                global_presence_item.home_objects.all()
            )
        )
    data = [{"name": item.name,
             "url": item.get_absolute_url(),
             "thumb": item.get_thumbnail_by_screen(screen)} for item in items]

    return json_response(data)


def json_get_mini_by_screen(request):
    """
    :return: devuelve las fotos de los items según la resolución para las
    miniaturas de la galería
    """
    screen = request.GET["screen"]
    category = get_object_or_404(Category, slug=request.GET["category"])
    # items = Item.home_objects.filter(category=category)
    items = category.all_home_item_set
    data = [{"name": item.name,
             "url": item.get_absolute_url(),
             "slug": item.slug,
             "thumb": item.get_mini_by_screen(screen)} for item in items]

    return json_response(data)


def json_get_slider_by_screen(request):
    """
    :return: devuelve las fotos de un item según la resolución
    """
    screen = request.GET["screen"]
    item = get_object_or_404(Item, slug=request.GET["item"])
    subitems = SubItem.objects.filter(item=item)
    data = [{"slider": subitem.get_photo_slider(screen),
             "videos": subitem.get_videos(screen),
             "slug": subitem.slug} for subitem in subitems]

    return json_response(data)
