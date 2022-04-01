from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtailmarkdown.blocks import MarkdownBlock

from puput.utils import get_image_model_path

import us

class CandidatesPage(Page):
    body = StreamField([
        ('paragraph', RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('markdown', MarkdownBlock(icon="code")),
        ('embed', EmbedBlock(max_width=800, max_height=400))
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body', classname="full"),
    ]

    # Parent page / subpage type rules
    parent_page_types = ['home.HomePage']
    subpage_types = [
        'candidates.StateCandidatePage',
        'candidates.UsSenateCandidatePage',
        'candidates.UsHouseCandidatePage',
        'candidates.StateSenateCandidatePage',
        'candidates.StateHouseCandidatePage',
        'candidates.CountyCandidatePage',
        'candidates.LocalCandidatePage',
        'candidates.LocalCouncilCandidatePage',
        'candidates.CountyCouncilCandidatePage',
        'candidates.SchoolDistrictCandidatePage',
        ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(
            request, *args, **kwargs)
        context['candidates'] = CandidatePage.objects.all()
        #context['candidates'] = CandidatePage.objects.order_by('state__title')
        return context


class CandidatePage(Page):
    STATE_CHOICES = list = [(k, v) for k, v in us.states.mapping('fips', 'name').items()]

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
        related_name='candidates',
    )

    office_type_ref = models.ForeignKey(
        'offices.OfficeType',
        verbose_name=_('office type'),
        on_delete=models.PROTECT,
        related_name='candidates',
    )

    office_ref = models.ForeignKey(
        'offices.Office',
        on_delete=models.PROTECT,
        related_name='candidates',
    )

    body = StreamField([
        ('paragraph', RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('markdown', MarkdownBlock(icon="code")),
        ('embed', EmbedBlock(max_width=800, max_height=400))
    ], blank=True)

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

    office_panels = []

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        FieldPanel('incumbent'),
        FieldPanel('featured'),
        StreamFieldPanel('body', classname="full"),

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
                FieldPanel('website'),
                FieldPanel('donate'),
            ],
            heading="Campaign Links",
        ),

        MultiFieldPanel(
            [
                FieldPanel('ballotpedia'),
                FieldPanel('wikipedia'),
            ],
            heading="Info Links",
        ),

    ]

    parent_page_types = []

    @classmethod
    def create_office_panels(cls):
        return []

class FederalCandidatePage(CandidatePage):
    pass
