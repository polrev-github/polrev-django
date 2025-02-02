from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList

from .state import StateCampaignPageBase
from offices.widgets import UsSenateOfficeChooser


class UsSenateCampaignPage(StateCampaignPageBase):
    class Meta:
        verbose_name = "U.S. Senate Campaign"

    us_senate_office_ref = models.ForeignKey(
        "offices.UsSenateOffice",
        verbose_name=_("office"),
        on_delete=models.PROTECT,
        related_name="us_senate_campaigns",
        null=True,
    )

    template = "campaigns/campaign_page.html"
    parent_page_types = ["campaigns.YearPage"]
    subpage_types = []

    office_panels = StateCampaignPageBase.office_panels + [
        FieldPanel(
            "us_senate_office_ref",
            widget=UsSenateOfficeChooser(
                linked_fields={
                    "state_ref": {"id": "id_state_ref"},
                    "office_type": {"title": "U.S. Senate"},
                }
            ),
        ),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(StateCampaignPageBase.content_panels, heading="Content"),
            ObjectList(office_panels, heading="Office"),
            ObjectList(StateCampaignPageBase.promote_panels, heading="Promote"),
            ObjectList(
                StateCampaignPageBase.settings_panels,
                heading="Settings",
                classname="settings",
            ),
        ]
    )

    def save(self, *args, **kwargs):
        self.area_ref = self.state_ref
        self.office_ref = self.us_senate_office_ref
        self.office_type_ref = self.office_ref.type_ref
        super().save(*args, **kwargs)
