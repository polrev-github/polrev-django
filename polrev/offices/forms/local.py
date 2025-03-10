from django.contrib.admin import site, widgets

from offices.models import LocalOffice
from .office import StateOfficeBaseForm


class LocalOfficeForm(StateOfficeBaseForm):
    class Meta:
        model = LocalOffice
        fields = StateOfficeBaseForm.Meta.fields + ["place_ref"]
        widgets = {
            "place_ref": widgets.AutocompleteSelect(
                LocalOffice.place_ref.field,
                site,
            ),
        }
