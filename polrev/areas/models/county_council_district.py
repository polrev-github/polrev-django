from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel

from areas.models.area import Area

from areas.widgets.county_widgets import CountyChooser

class CountyCouncilDistrict(Area):
    state_ref = models.ForeignKey(
        'areas.State',
        verbose_name=_('State'),
        on_delete=models.PROTECT,
        related_name='county_council_districts'
    )

    county_ref = models.ForeignKey(
        'areas.County',
        verbose_name=_('County'),
        on_delete=models.PROTECT,
        related_name='county_council_districts'
    )

    panels = Area.panels + [
        FieldPanel('state_ref'),
        FieldPanel('county_ref', widget=CountyChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'}
        })),
    ]

    def save(self, *args, **kwargs):
        self.kind = self.KIND_COUNTY_COUNCIL_DISTRICT
        self.title = f"{self.county_ref.title}, {self.name}"
        super().save(*args, **kwargs)
