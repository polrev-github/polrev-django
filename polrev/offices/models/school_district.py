from django.db import models

from wagtail.admin.panels import FieldPanel

from .state import StateOfficeBase
from areas.widgets.school_district_widgets import SchoolDistrictChooser

class SchoolDistrictOffice(StateOfficeBase):

    class Meta:
        verbose_name = "School District Office"

    district_ref = models.ForeignKey(
        'areas.SchoolDistrict',
        verbose_name='district',
        on_delete=models.PROTECT,
        related_name='school_district_offices',
    )

    area_panels = StateOfficeBase.area_panels + [
        FieldPanel('district_ref', widget=SchoolDistrictChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'}
        })),
    ]

    panels = area_panels + StateOfficeBase.other_panels

    def save(self, *args, **kwargs):
        self.area_ref = self.district_ref
        super().save(*args, **kwargs)
