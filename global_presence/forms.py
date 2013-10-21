# -*- coding: utf-8 -*-
""" global_presence's forms """

from django import forms
from tinymce.widgets import TinyMCE

from .models import Item, Team


class ItemAdminForm(forms.ModelForm):
    """ Item form for django admin interface """

    class Meta:
        model = Item

    def __init__(self, *args, **kwargs):
        """ customizin description widget """
        super(ItemAdminForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget = TinyMCE(
            attrs={'rows': 20, 'cols': 50})


class TeamAdminForm(forms.ModelForm):
    """ Team form for django admin interface """

    class Meta:
        model = Team

    def __init__(self, *args, **kwargs):
        """ customizin the order of the fields """
        super(TeamAdminForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = [
            'name', 'address_line_1', 'address_line_2','address_line_3',
            'address_line_4', 'phone', 'email', 'image', 'country'
        ]
