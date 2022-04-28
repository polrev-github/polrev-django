from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.search import index
from wagtail.admin.edit_handlers import FieldPanel

from areas.models import Area


class StateJudicialDistrict(Area):
    class Meta:
        ordering = ['number']

    def __init__(self, *args, **kwargs):        
        super().__init__(*args, **kwargs)
        self.kind = self.KIND_STATE_JUDICIAL_DISTRICT

    state_ref = models.ForeignKey(
        'areas.State',
        verbose_name=_('State'),
        on_delete=models.PROTECT,
        related_name='state_judicial_districts'
    )

    number = models.PositiveSmallIntegerField()
    
    panels = Area.panels + [
        FieldPanel('state_ref'),
        FieldPanel('number'),
    ]

    search_fields = Area.search_fields + [
        index.FilterField('state_ref_id')
    ]

    def save(self, *args, **kwargs):
        self.kind = self.KIND_STATE_JUDICIAL_DISTRICT
        self.state_fips = self.state_ref.state_fips
        self.title = f"{self.state_ref.name} {self.name}"
        super().save(*args, **kwargs)
