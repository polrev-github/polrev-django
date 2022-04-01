from django import forms
from django.contrib.admin import site, widgets

from areas.models import LocalCouncilDistrict
from .area_forms import AreaForm

class LocalCouncilDistrictForm(AreaForm):

    class Meta:
        model = LocalCouncilDistrict
        fields = AreaForm.Meta.fields + ['state_ref', 'place_ref']
        widgets = {
            'place_ref': widgets.AutocompleteSelect(
                LocalCouncilDistrict.place_ref.field,
                site,
            ),
        }
