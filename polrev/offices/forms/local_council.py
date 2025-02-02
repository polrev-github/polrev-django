from django.contrib.admin import site, widgets

from offices.models import LocalCouncilOffice
from .office import StateOfficeBaseForm


class LocalCouncilOfficeForm(StateOfficeBaseForm):

    class Meta:
        model = LocalCouncilOffice
        fields = StateOfficeBaseForm.Meta.fields + ["place_ref", "district_ref"]
        widgets = {
            "place_ref": widgets.AutocompleteSelect(
                LocalCouncilOffice.place_ref.field,
                site,
            ),
        }
