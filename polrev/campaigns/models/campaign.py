import datetime
from django.utils import timezone
import us

from django.db import models
from django.utils.translation import gettext_lazy as _

from modelcluster.fields import ParentalManyToManyField
from wagtail.models import Page
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.fields import StreamField, RichTextField
from wagtail.search import index
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel, PageChooserPanel
from wagtail.admin.panels import FieldPanel
from wagtailautocomplete.edit_handlers import AutocompletePanel

from wagtail.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtailmarkdown.blocks import MarkdownBlock

from puput.utils import get_image_model_path

import us

class CampaignPage(Page):

    STATUS_RUNNING = 0
    STATUS_DROPPED_OUT = 1
    STATUS_WON_PRIMARY = 2
    STATUS_LOST_PRIMARY = 3
    STATUS_WON_RACE = 4
    STATUS_LOST_RACE = 5

    STATUS_MAP = {
        STATUS_RUNNING: 'Running',
        STATUS_DROPPED_OUT: 'Dropped Out',
        STATUS_WON_PRIMARY: 'Won Primary',
        STATUS_LOST_PRIMARY: 'Lost Primary',
        STATUS_WON_RACE: 'Won Race',
        STATUS_LOST_RACE: 'Lost Race'
    }

    STATUS_CHOICES = [(k, v) for k, v in STATUS_MAP.items()]
    IMPOTENT_LIST = [STATUS_DROPPED_OUT, STATUS_LOST_PRIMARY]

    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=STATUS_RUNNING)
    potent = models.BooleanField(default=True)

    STATE_CHOICES = [(k, v) for k, v in us.states.mapping('fips', 'name').items()]

    state_fips = models.CharField(
        choices=STATE_CHOICES,
        verbose_name=_('State FIPS'),
        max_length=2,
        help_text=_("Example: 01, 02 ... 50"),
        default = '00'
    )

    area_ref = models.ForeignKey(
        'areas.Area',
        on_delete=models.PROTECT,
        related_name='campaigns',
    )

    office_type_ref = models.ForeignKey(
        'offices.OfficeType',
        verbose_name=_('office type'),
        on_delete=models.PROTECT,
        related_name='campaigns',
    )

    office_ref = models.ForeignKey(
        'offices.Office',
        on_delete=models.PROTECT,
        related_name='campaigns',
    )

    date = models.DateTimeField(verbose_name=_("Election date"), default=timezone.now)

    body = StreamField([
        ('paragraph', RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('markdown', MarkdownBlock(icon="code")),
        ('embed', EmbedBlock(max_width=800, max_height=400))
    ], blank=True)
    
    excerpt = RichTextField(
        verbose_name=_('excerpt'),
        blank=True,
        help_text=_("Entry excerpt to be displayed on entries list. "
                    "If this field is not filled, a truncated version of body text will be used.")
    )

    image = models.ForeignKey(
        get_image_model_path(),
        verbose_name=_('Image'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    incumbent = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)

    # Social Media Links
    facebook = models.URLField("facebook", blank=True)
    twitter = models.URLField("twitter", blank=True)
    instagram = models.URLField("instagram", blank=True)

    # Campaign Links
    website = models.URLField("website", blank=True)
    donate = models.URLField("donate", blank=True)

    # Info Links
    ballotpedia = models.URLField("ballotpedia", blank=True)
    wikipedia = models.URLField("wikipedia", blank=True)

    # Parties and Endorsements
    '''
    parties = ParentalManyToManyField(
        'parties.Party',
        blank=True,
        related_name='campaigns'
    )
    '''
    endorsements = ParentalManyToManyField(
        'parties.Party',
        blank=True,
        related_name='endorsed_campaigns'
    )

    office_panels = []

    content_panels = Page.content_panels + [
        FieldPanel('status'),
        FieldPanel('image'),
        #AutocompletePanel('parties', target_model='parties.Party'),
        AutocompletePanel('endorsements', target_model='parties.Party'),
        FieldPanel('incumbent'),
        FieldPanel('featured'),
        FieldPanel('body', classname="full"),
        FieldPanel('excerpt'),

        MultiFieldPanel(
            [
                FieldPanel('website'),
                FieldPanel('donate'),
            ],
            heading="Campaign Links",
        ),

        MultiFieldPanel(
            [
                FieldPanel('facebook'),
                FieldPanel('twitter'),
                FieldPanel('instagram'),
            ],
            heading="Social Media Links",
        ),

        MultiFieldPanel(
            [
                FieldPanel('ballotpedia'),
                FieldPanel('wikipedia'),
            ],
            heading="Info Links",
        ),

    ]

    parent_page_types = ['campaigns.YearPage']


    search_fields = Page.search_fields + [
        #index.SearchField('body'),
        index.FilterField('potent')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['campaign'] = self

        return context

    def save(self, *args, **kwargs):
        self.potent = False if self.status in self.IMPOTENT_LIST else True

        super().save(*args, **kwargs)

class FederalCampaignPage(CampaignPage):
    pass
