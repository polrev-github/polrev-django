from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.panels import FieldPanel

from areas.models.area import Area

from areas.widgets.place_widgets import PlaceChooser

class LocalCouncilDistrict(Area):
    state_ref = models.ForeignKey(
        'areas.State',
        verbose_name=_('State'),
        on_delete=models.PROTECT,
        related_name='local_council_districts'
    )

    place_ref = models.ForeignKey(
        'areas.Place',
        verbose_name=_('Place'),
        on_delete=models.PROTECT,
        related_name='local_council_districts'
    )

    panels = Area.panels + [
        FieldPanel('state_ref'),
        FieldPanel('place_ref', widget=PlaceChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'}
        })),
    ]

    def save(self, *args, **kwargs):
        self.kind = self.KIND_LOCAL_COUNCIL_DISTRICT
        #self.title = f"{self.state_ref.name} {self.name}"
        self.state_fips = self.state_ref.state_fips
        super().save(*args, **kwargs)
