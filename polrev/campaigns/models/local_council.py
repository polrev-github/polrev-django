from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList

from .local import LocalCampaignPageBase
from areas.widgets.local_council_district_widgets import LocalCouncilDistrictChooser
from offices.widgets import OfficeTypeChooser, LocalCouncilOfficeChooser


class LocalCouncilCampaignPage(LocalCampaignPageBase):

    class Meta:
        verbose_name = "Local Council Campaign"

    district_ref = models.ForeignKey(
        "areas.LocalCouncilDistrict",
        verbose_name=_("district"),
        on_delete=models.PROTECT,
        related_name="local_council_campaigns",
    )

    local_council_office_ref = models.ForeignKey(
        "offices.LocalCouncilOffice",
        verbose_name=_("office"),
        on_delete=models.PROTECT,
        related_name="local_council_campaigns",
        null=True,
    )

    office_panels = LocalCampaignPageBase.office_panels + [
        FieldPanel(
            "district_ref",
            widget=LocalCouncilDistrictChooser(
                linked_fields={
                    "state_ref": {"id": "id_state_ref"},
                    "place_ref": {"id": "id_place_ref"},
                }
            ),
        ),
        FieldPanel(
            "office_type_ref",
            widget=OfficeTypeChooser(
                linked_fields={
                    "state_ref": {
                        "id": "id_state_ref"
                    }  # TODO:  Unused but keep.  Filter by area?
                }
            ),
        ),
        FieldPanel(
            "local_council_office_ref",
            widget=LocalCouncilOfficeChooser(
                linked_fields={
                    "state_ref": {"id": "id_state_ref"},
                    "place_ref": {"id": "id_place_ref"},
                    "district_ref": {"id": "id_district_ref"},
                    "office_type_ref": {"id": "id_office_type_ref"},
                    "office_type": {"title": "City Council"},
                }
            ),
        ),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(LocalCampaignPageBase.content_panels, heading="Content"),
            ObjectList(office_panels, heading="Office"),
            ObjectList(LocalCampaignPageBase.promote_panels, heading="Promote"),
            ObjectList(
                LocalCampaignPageBase.settings_panels,
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
        self.office_ref = self.local_council_office_ref
        super().save(*args, **kwargs)
