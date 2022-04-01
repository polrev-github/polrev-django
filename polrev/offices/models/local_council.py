from django.db import models

from wagtail.admin.edit_handlers import FieldPanel

from .local import LocalOffice
from areas.widgets.local_council_district_widgets import LocalCouncilDistrictChooser

class LocalCouncilOffice(LocalOffice):

    class Meta:
        verbose_name = "Local Council Office"

    district_ref = models.ForeignKey(
        'areas.LocalCouncilDistrict',
        verbose_name='district',
        on_delete=models.PROTECT,
        related_name='local_council_offices',
    )

    area_panels = LocalOffice.area_panels + [
        FieldPanel('district_ref', widget=LocalCouncilDistrictChooser(linked_fields={
            'place_ref': {'id': 'id_place_ref'}
        })),
    ]

    panels = area_panels + LocalOffice.other_panels

    def save(self, *args, **kwargs):
        self.area_ref = self.place_ref
        super().save(*args, **kwargs)
