from django import forms
from django.contrib.admin import site, widgets

from areas.models import CountyCouncilDistrict
from .area_forms import AreaForm

class CountyCouncilDistrictForm(AreaForm):

    class Meta:
        model = CountyCouncilDistrict
        fields = AreaForm.Meta.fields + ['state_ref', 'county_ref']
        widgets = {
            'place_ref': widgets.AutocompleteSelect(
                CountyCouncilDistrict.county_ref.field,
                site,
            ),
        }
