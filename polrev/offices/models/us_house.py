from django.db import models

from wagtail.admin.panels import FieldPanel

from .state import StateOfficeBase
from areas.widgets.congressional_district_widgets import CongressionalDistrictChooser

class UsHouseOffice(StateOfficeBase):

    class Meta:
        verbose_name = "US House Office"

    district_ref = models.ForeignKey(
        'areas.CongressionalDistrict',
        on_delete=models.PROTECT,
        related_name='us_house_offices',
    )

    area_panels = StateOfficeBase.area_panels + [
            FieldPanel('district_ref', widget=CongressionalDistrictChooser(linked_fields={
                'state_ref': {'id': 'id_state_ref'}
            })),
        ]

    panels = area_panels + StateOfficeBase.other_panels
    
    def save(self, *args, **kwargs):
        self.area_ref = self.district_ref
        super().save(*args, **kwargs)
