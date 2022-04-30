from django.db import models

from wagtail.admin.edit_handlers import FieldPanel

from .county import CountyOffice
from areas.widgets.county_judicial_precinct_widgets import CountyJudicialPrecinctChooser

class CountyJudicialPrecinctOffice(CountyOffice):

    class Meta:
        verbose_name = "County Judicial Precinct Office"

    district_ref = models.ForeignKey(
        'areas.CountyJudicialPrecinct',
        verbose_name='district',
        on_delete=models.PROTECT,
        related_name='county_judicial_precinct_offices',
    )

    area_panels = CountyOffice.area_panels + [
        FieldPanel('district_ref', widget=CountyJudicialPrecinctChooser(linked_fields={
            'county_ref': {'id': 'id_county_ref'}
        })),
    ]

    panels = area_panels + CountyOffice.other_panels

    def save(self, *args, **kwargs):
        self.area_ref = self.district_ref
        super().save(*args, **kwargs)
