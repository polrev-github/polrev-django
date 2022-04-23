from django.db import models
from django.utils.translation import ugettext_lazy as _

from modelcluster.models import ClusterableModel

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, PageChooserPanel

from colorfield.fields import ColorField

class Party(ClusterableModel):

    class Meta:
        verbose_name_plural = 'Parties'
        ordering = ['title']

    title = models.TextField(
        verbose_name=_('title'),
        help_text=_("Example: Working Families Party")
    )

    abbrev = models.CharField(
        verbose_name=_('abbreviation'),
        max_length=16,
        help_text=_("Example: WFP")
    )

    color = ColorField(default='#FF0000')

    website = models.URLField("website", blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('abbrev'),
        FieldPanel('color'),
        FieldPanel('website'),
    ]

    @classmethod
    def autocomplete_create(kls: type, value: str):
        return kls.objects.create(title=value)

    def __str__(self):
        return self.title
