# -*- coding: utf-8 -*-

"""
Copyright (C) 2011 Dariusz Suchojad <dsuch at gefira.pl>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# Django
from django import forms

# Zato
from zato.admin.web.forms import ChooseClusterForm as _ChooseClusterForm

class CreateForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'style':'width:100%'}))
    is_active = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'checked':'checked'}))
    url_path = forms.CharField(widget=forms.TextInput(attrs={'style':'width:50%'}))
    method = forms.CharField(widget=forms.TextInput(attrs={'style':'width:20%'}))
    soap_action = forms.CharField(widget=forms.TextInput(attrs={'style':'width:100%'}))
    connection = forms.CharField(widget=forms.HiddenInput())
    transport = forms.CharField(widget=forms.HiddenInput())

class EditForm(CreateForm):
    is_active = forms.BooleanField(required=False, widget=forms.CheckboxInput())

class ChooseClusterForm(_ChooseClusterForm):
    connection = forms.CharField(widget=forms.HiddenInput())
    transport = forms.CharField(widget=forms.HiddenInput())