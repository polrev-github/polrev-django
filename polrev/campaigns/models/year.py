from django.utils.translation import gettext_lazy as _

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

from wagtail.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtailmarkdown.blocks import MarkdownBlock

import us

from .campaign import *
from .campaigns_base import CampaignsPageBase


class YearPage(CampaignsPageBase):
    template = "campaigns/campaigns_page.html"

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
        FieldPanel("body", classname="full"),
    ]

    # Parent page / subpage type rules
    parent_page_types = ["campaigns.CampaignsPage"]
    subpage_types = [
        "campaigns.StateCampaignPage",
        "campaigns.UsSenateCampaignPage",
        "campaigns.UsHouseCampaignPage",
        "campaigns.StateSenateCampaignPage",
        "campaigns.StateHouseCampaignPage",
        "campaigns.SchoolDistrictCampaignPage",
        "campaigns.CountyCampaignPage",
        "campaigns.LocalCampaignPage",
        "campaigns.LocalCouncilCampaignPage",
        "campaigns.CountyCouncilCampaignPage",
        "campaigns.StateJudicialDistrictCampaignPage",
    ]

    def get_campaigns(self):
        campaigns = (
            CampaignPage.objects.child_of(self)
            .live()
            .order_by("state_fips", "office_type_ref__rank", "office_ref__number")
        )
        return campaigns

    def get_state_campaigns(self, state_fips):
        campaigns = (
            CampaignPage.objects.child_of(self)
            .live()
            .filter(state_fips=state_fips)
            .order_by("office_type_ref__rank", "office_ref__number")
        )
        return campaigns
