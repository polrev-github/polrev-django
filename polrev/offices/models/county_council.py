from django.db import models

from wagtail.admin.panels import FieldPanel

from .county import CountyOfficeBase
from areas.widgets.county_council_district_widgets import CountyCouncilDistrictChooser

class CountyCouncilOffice(CountyOfficeBase):

    class Meta:
        verbose_name = "County Council Office"

    district_ref = models.ForeignKey(
        'areas.CountyCouncilDistrict',
        verbose_name='district',
        on_delete=models.PROTECT,
        related_name='county_council_offices',
    )

    area_panels = CountyOfficeBase.area_panels + [
        FieldPanel('district_ref', widget=CountyCouncilDistrictChooser(linked_fields={
            'county_ref': {'id': 'id_county_ref'}
        })),
    ]

    panels = area_panels + CountyOfficeBase.other_panels

    def save(self, *args, **kwargs):
        self.area_ref = self.district_ref
        super().save(*args, **kwargs)
