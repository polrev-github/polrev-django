from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel, TabbedInterface, ObjectList

from .state import StateCampaignPageBase
from areas.widgets.place_widgets import PlaceChooser
from areas.widgets.local_council_district_widgets import LocalCouncilDistrictChooser
from offices.widgets import OfficeTypeChooser, LocalCouncilOfficeChooser

class LocalCouncilCampaignPage(StateCampaignPageBase):

    class Meta:
        verbose_name = "Local Council Campaign"

    place_ref = models.ForeignKey(
        'areas.Place',
        verbose_name=_('place'),
        on_delete=models.PROTECT,
        related_name='local_council_campaigns',
    )

    district_ref = models.ForeignKey(
        'areas.LocalCouncilDistrict',
        verbose_name=_('district'),
        on_delete=models.PROTECT,
        related_name='local_council_campaigns',
    )

    local_council_office_ref = models.ForeignKey(
        'offices.LocalCouncilOffice',
        verbose_name=_('office'),
        on_delete=models.PROTECT,
        related_name='local_council_campaigns',
        null=True,
    )

    office_panels = StateCampaignPageBase.office_panels + [
        FieldPanel('place_ref', widget=PlaceChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'}
        })),
        FieldPanel('district_ref', widget=LocalCouncilDistrictChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'},
            'place_ref': {'id': 'id_place_ref'}
        })),
        FieldPanel('office_type_ref', widget=OfficeTypeChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'} # TODO:  Unused but keep.  Filter by area?
        })),
        FieldPanel('local_council_office_ref', widget=LocalCouncilOfficeChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'},
            'place_ref': {'id': 'id_place_ref'},
            'district_ref': {'id': 'id_district_ref'},
            'office_type_ref': {'id': 'id_office_type_ref'},
        })),
    ]

    edit_handler = TabbedInterface([
        ObjectList(StateCampaignPageBase.content_panels, heading='Content'),
        ObjectList(office_panels, heading='Office'),
        ObjectList(StateCampaignPageBase.promote_panels, heading='Promote'),
        ObjectList(StateCampaignPageBase.settings_panels, heading='Settings', classname="settings"),
    ])

    parent_page_types = ['campaigns.YearPage']
    subpage_types = []
    

    def save(self, *args, **kwargs):
        self.area_ref = self.district_ref
        self.office_ref = self.local_council_office_ref
        super().save(*args, **kwargs)
