from django.db import models

from wagtail.admin.edit_handlers import FieldPanel

from .state import StateOfficeBase
from areas.widgets.place_widgets import PlaceChooser

class LocalOfficeBase(StateOfficeBase):

    place_ref = models.ForeignKey(
        'areas.Place',
        verbose_name='place',
        on_delete=models.PROTECT,
        related_name='local_offices',
    )

    area_panels = StateOfficeBase.area_panels + [
        FieldPanel('place_ref', widget=PlaceChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'}
        })),
    ]

class LocalOffice(LocalOfficeBase):

    class Meta:
        verbose_name = "Local Office"

    panels = LocalOfficeBase.area_panels + StateOfficeBase.other_panels

    def save(self, *args, **kwargs):
        self.area_ref = self.place_ref
        super().save(*args, **kwargs)
