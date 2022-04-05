from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtailautocomplete.edit_handlers import AutocompletePanel

from .state import StateOfficeBase
from areas.widgets.legislate_district_widgets import StateSenateDistrictChooser

class StateSenateOffice(StateOfficeBase):

    class Meta:
        verbose_name = "State Senate Office"

    district_ref = models.ForeignKey(
        'areas.StateSenateDistrict',
        on_delete=models.PROTECT,
        related_name='state_senate_offices',
    )

    area_panels = StateOfficeBase.area_panels + [
        FieldPanel('district_ref', widget=StateSenateDistrictChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'}
        })),
    ]

    panels = area_panels + StateOfficeBase.other_panels

    def save(self, *args, **kwargs):
        self.area_ref = self.district_ref
        super().save(*args, **kwargs)
