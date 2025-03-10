from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, PageChooserPanel

from wagtail.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtailmarkdown.blocks import MarkdownBlock

from .campaign import *
from .campaigns_base import CampaignsPageBase


class CampaignsPage(CampaignsPageBase):

    year_page = models.ForeignKey(
        "campaigns.YearPage",
        related_name="+",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    body = StreamField(
        [
            ("paragraph", RichTextBlock()),
            ("image", ImageChooserBlock()),
            ("markdown", MarkdownBlock(icon="code")),
            ("embed", EmbedBlock(max_width=800, max_height=400)),
        ],
        blank=True,
    )

    content_panels = Page.content_panels + [
        PageChooserPanel("year_page", "campaigns.YearPage"),
        FieldPanel("body", classname="full"),
    ]

    parent_page_types = ["home.HomePage"]
    subpage_types = [
        "campaigns.YearPage",
    ]

    def get_campaigns(self):
        campaigns = (
            CampaignPage.objects.child_of(self.year_page)
            .live()
            .filter(potent=True)
            .order_by("state_fips", "office_type_ref__rank", "office_ref__number")
        )
        return campaigns

    def get_state_campaigns(self, state_fips):
        campaigns = (
            CampaignPage.objects.child_of(self.year_page)
            .live()
            .filter(potent=True, state_fips=state_fips)
            .order_by("office_type_ref__rank", "office_ref__number")
        )
        return campaigns
