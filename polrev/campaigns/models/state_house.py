from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList

from .state import StateCampaignPageBase
from areas.widgets.legislate_district_widgets import StateHouseDistrictChooser
from offices.widgets import StateHouseOfficeChooser


class StateHouseCampaignPage(StateCampaignPageBase):

    class Meta:
        verbose_name = "State House Campaign"

    district_ref = models.ForeignKey(
        "areas.StateHouseDistrict",
        on_delete=models.PROTECT,
        related_name="state_house_campaigns",
    )

    state_house_office_ref = models.ForeignKey(
        "offices.StateHouseOffice",
        verbose_name=_("office"),
        on_delete=models.PROTECT,
        related_name="state_house_campaigns",
        null=True,
    )

    office_panels = StateCampaignPageBase.office_panels + [
        FieldPanel(
            "district_ref",
            widget=StateHouseDistrictChooser(
                linked_fields={"state_ref": {"id": "id_state_ref"}}
            ),
        ),
        FieldPanel(
            "state_house_office_ref",
            widget=StateHouseOfficeChooser(
                linked_fields={
                    "state_ref": {"id": "id_state_ref"},
                    "district_ref": {"id": "id_district_ref"},
                    "office_type": {"title": "State House"},
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
        self.office_ref = self.state_house_office_ref
        self.office_type_ref = self.office_ref.type_ref
        super().save(*args, **kwargs)
