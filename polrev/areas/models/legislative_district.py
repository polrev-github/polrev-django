from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel

from areas.models import Area


class LegislativeDistrict(Area):
    class Meta:
        ordering = ['district_num']

    district_num = models.PositiveSmallIntegerField()
    seats = models.PositiveSmallIntegerField()
    
    panels = Area.panels + [
        FieldPanel('district_num'),
        FieldPanel('seats'),
    ]


class StateSenateDistrict(LegislativeDistrict):
    state_ref = models.ForeignKey(
        'areas.State',
        verbose_name=_('State'),
        on_delete=models.PROTECT,
        related_name='state_senate_districts'
    )

    def save(self, *args, **kwargs):
        self.kind = self.KIND_STATE_SENATE_DISTRICT
        self.name = f"State Senate District {self.district_num}"
        self.title = f"{self.state_ref.name} {self.name}"
        super().save(*args, **kwargs)


class StateHouseDistrict(LegislativeDistrict):
    state_ref = models.ForeignKey(
        'areas.State',
        verbose_name=_('State'),
        on_delete=models.PROTECT,
        related_name='state_house_districts'
    )

    def save(self, *args, **kwargs):
        self.kind = self.KIND_STATE_HOUSE_DISTRICT
        self.name = f"State House District {self.district_num}"
        self.title = f"{self.state_ref.name} {self.name}"
        super().save(*args, **kwargs)
