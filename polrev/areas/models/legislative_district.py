from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.search import index
from wagtail.admin.panels import FieldPanel

from areas.models import Area


class LegislativeDistrict(Area):
    class Meta:
        ordering = ["district_num"]

    district_num = models.PositiveSmallIntegerField()
    seats = models.PositiveSmallIntegerField()

    panels = Area.panels + [
        FieldPanel("state_ref"),
        FieldPanel("district_num"),
        FieldPanel("seats"),
    ]


class StateSenateDistrict(LegislativeDistrict):
    state_ref = models.ForeignKey(
        "areas.State",
        verbose_name=_("State"),
        on_delete=models.PROTECT,
        related_name="state_senate_districts",
    )

    search_fields = Area.search_fields + [
        index.FilterField("state_ref_id"),
    ]

    def save(self, *args, **kwargs):
        self.kind = self.KIND_STATE_SENATE_DISTRICT
        self.name = f"State Senate District {self.district_num}"
        self.state_fips = self.state_ref.state_fips
        self.title = f"{self.state_ref.name} {self.name}"
        super().save(*args, **kwargs)


class StateHouseDistrict(LegislativeDistrict):
    state_ref = models.ForeignKey(
        "areas.State",
        verbose_name=_("State"),
        on_delete=models.PROTECT,
        related_name="state_house_districts",
    )

    search_fields = Area.search_fields + [
        index.FilterField("state_ref_id"),
    ]

    def save(self, *args, **kwargs):
        self.kind = self.KIND_STATE_HOUSE_DISTRICT
        self.name = f"State House District {self.district_num}"
        self.state_fips = self.state_ref.state_fips
        self.title = f"{self.state_ref.name} {self.name}"
        super().save(*args, **kwargs)
