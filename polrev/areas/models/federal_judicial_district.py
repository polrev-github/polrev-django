from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.search import index
from wagtail.admin.panels import FieldPanel

from areas.models import Area


class FederalJudicialDistrict(Area):
    class Meta:
        ordering = ['number']

    state_ref = models.ForeignKey(
        'areas.State',
        verbose_name=_('State'),
        on_delete=models.PROTECT,
        related_name='federal_judicial_districts'
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
        self.kind = self.KIND_FEDERAL_JUDICIAL_DISTRICT
        self.title = f"{self.name}"
        super().save(*args, **kwargs)
