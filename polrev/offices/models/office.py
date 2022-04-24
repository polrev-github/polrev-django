from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

import us

from model_utils.managers import InheritanceManager

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, PageChooserPanel


class Office(models.Model):
    STATE_CHOICES = list = [(k, v) for k, v in us.states.mapping('fips', 'name').items()]

    class Meta:
        ordering = ['title']

    type_ref = models.ForeignKey(
        'offices.OfficeType',
        verbose_name=_('Office Type'),
        on_delete=models.PROTECT,
        related_name='offices'
    )

    state_fips = models.CharField(
        choices=STATE_CHOICES,
        verbose_name=_('State FIPS'),
        max_length=2,
        help_text=_("Example: 01, 02 ... 50"),
        default = '00'
    )

    area_ref = models.ForeignKey(
        'areas.Area',
        verbose_name=_('Area'),
        on_delete=models.PROTECT,
        related_name='offices'
    )

    title = models.CharField(
        verbose_name=_('title'),
        max_length=256,
        help_text=_("Example: U.S. Senate, Ohio")
    )

    website = models.URLField("website", blank=True)

    area_panels = []

    other_panels = [
        FieldPanel('website'),
    ]

    def __str__(self):
        return self.title

class FederalOffice(Office):
    pass
