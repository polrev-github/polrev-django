import datetime
import imp
from django.utils import timezone
import us

from django.db import models
from django.utils.translation import ugettext_lazy as _

from modelcluster.fields import ParentalManyToManyField
from wagtail.core.models import Page
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.fields import StreamField
from wagtail.search import index
from wagtail.admin.edit_handlers import StreamFieldPanel, RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailautocomplete.edit_handlers import AutocompletePanel

from wagtail.core.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtailmarkdown.blocks import MarkdownBlock

import us

from .election import *
from .elections_base import ElectionsPageBase

class ElectionsPage(ElectionsPageBase):

    year_page = models.ForeignKey(
        'elections.YearPage',
        related_name='+',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        )

    body = StreamField([
        ('paragraph', RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('markdown', MarkdownBlock(icon="code")),
        ('embed', EmbedBlock(max_width=800, max_height=400))
    ], blank=True)

    content_panels = Page.content_panels + [
        PageChooserPanel('year_page', 'elections.YearPage'),
        StreamFieldPanel('body', classname="full"),
    ]

    parent_page_types = ['home.HomePage']
    subpage_types = [
        'elections.YearPage',
    ]
    '''
    def get_elections(self):
        elections = ElectionPage.objects.live().order_by('state_fips', 'office_type_ref__rank', 'office_ref__number')
        return elections

    def get_state_elections(self, state_fips):
        elections = ElectionPage.objects.live().filter(state_fips=state_fips).order_by('office_type_ref__rank', 'office_ref__number')
        return elections
    '''

    def get_elections(self):
        elections = ElectionPage.objects.child_of(self.year_page).live().filter(potent=True).order_by('state_fips', 'office_type_ref__rank', 'office_ref__number')
        return elections

    def get_state_elections(self, state_fips):
        elections = ElectionPage.objects.child_of(self.year_page).live().filter(potent=True, state_fips=state_fips).order_by('office_type_ref__rank', 'office_ref__number')
        return elections
