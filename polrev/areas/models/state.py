from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel

from areas.models import Area


class State(Area):
    state_usps = models.CharField(
        verbose_name=_('State USPS Code'),
        max_length=2,
        help_text=_("Example: AL, AK ... WY"),
    )

    panels = Area.panels + [
        FieldPanel('state_usps'),
        FieldPanel('state_fips'),
    ]

    def save(self, *args, **kwargs):
        self.kind = self.KIND_STATE
        self.title = self.name
        super().save(*args, **kwargs)
