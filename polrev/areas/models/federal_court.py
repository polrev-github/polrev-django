from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.search import index
from wagtail.admin.edit_handlers import FieldPanel

from areas.models import Area


class FederalCourt(Area):
    class Meta:
        ordering = ['number']

    number = models.PositiveSmallIntegerField()
    
    panels = Area.panels + [
        FieldPanel('number'),
    ]

    def save(self, *args, **kwargs):
        self.kind = self.KIND_FEDERAL_COURT
        self.title = f"{self.name}"
        super().save(*args, **kwargs)
