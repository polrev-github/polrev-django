from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList

from .state import StateCampaignPageBase
from areas.widgets.legislate_district_widgets import StateSenateDistrictChooser
from offices.widgets import StateSenateOfficeChooser


class StateSenateCampaignPage(StateCampaignPageBase):

    class Meta:
        verbose_name = "State Senate Campaign"

    district_ref = models.ForeignKey(
        "areas.StateSenateDistrict",
        verbose_name=_("district"),
        on_delete=models.PROTECT,
        related_name="state_senate_campaigns",
    )

    state_senate_office_ref = models.ForeignKey(
        "offices.StateSenateOffice",
        verbose_name=_("office"),
        on_delete=models.PROTECT,
        related_name="state_senate_campaigns",
        null=True,
    )

    office_panels = StateCampaignPageBase.office_panels + [
        FieldPanel(
            "district_ref",
            widget=StateSenateDistrictChooser(
                linked_fields={"state_ref": {"id": "id_state_ref"}}
            ),
        ),
        FieldPanel(
            "state_senate_office_ref",
            widget=StateSenateOfficeChooser(
                linked_fields={
                    "state_ref": {"id": "id_state_ref"},
                    "district_ref": {"id": "id_district_ref"},
                    "office_type": {"title": "State Senate"},
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

    template = "campaigns/campaign_page.html"
    parent_page_types = ["campaigns.YearPage"]
    subpage_types = []

    def save(self, *args, **kwargs):
        self.area_ref = self.district_ref
        self.office_ref = self.state_senate_office_ref
        self.office_type_ref = self.office_ref.type_ref
        super().save(*args, **kwargs)
