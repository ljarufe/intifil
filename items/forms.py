# -*- coding: utf-8 -*-

from django import forms
from items.models import Item


class OrderForm(forms.Form):
    """
    Formulario para ordenar los items en la página de inicio
    """
    order = forms.CharField(widget=forms.HiddenInput)

    def reorder_items(self):
        order_list = self.cleaned_data["order"].split()
        map(Item.set_order, order_list, range(len(order_list)))