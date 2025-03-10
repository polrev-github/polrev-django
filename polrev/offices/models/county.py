from django.db import models

from wagtail.admin.panels import FieldPanel

from .state import StateOfficeBase
from areas.widgets.county_widgets import CountyChooser


class CountyOfficeBase(StateOfficeBase):

    county_ref = models.ForeignKey(
        "areas.County",
        verbose_name="county",
        on_delete=models.PROTECT,
        related_name="county_offices",
    )

    area_panels = StateOfficeBase.area_panels + [
        FieldPanel(
            "county_ref",
            widget=CountyChooser(linked_fields={"state_ref": {"id": "id_state_ref"}}),
        ),
    ]


class CountyOffice(CountyOfficeBase):

    class Meta:
        verbose_name = "County Office"

    panels = CountyOfficeBase.area_panels + StateOfficeBase.other_panels

    def save(self, *args, **kwargs):
        self.area_ref = self.county_ref
        super().save(*args, **kwargs)
