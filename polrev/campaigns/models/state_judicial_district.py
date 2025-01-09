from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList

from .state import StateCampaignPageBase
from areas.widgets.state_judicial_district_widgets import StateJudicialDistrictChooser
from offices.widgets import OfficeTypeChooser, StateJudicialDistrictOfficeChooser

class StateJudicialDistrictCampaignPage(StateCampaignPageBase):

    class Meta:
        verbose_name = "State Judicial District Campaign"

    district_ref = models.ForeignKey(
        'areas.StateJudicialDistrict',
        on_delete=models.PROTECT,
        related_name='state_judicial_district_campaigns',
    )

    state_judicial_district_office_ref = models.ForeignKey(
        'offices.StateJudicialDistrictOffice',
        verbose_name=_('office'),
        on_delete=models.PROTECT,
        related_name='state_judicial_district_campaigns',
        null=True,
    )

    office_panels = StateCampaignPageBase.office_panels + [
        FieldPanel('district_ref', widget=StateJudicialDistrictChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'}
        })),
        FieldPanel('office_type_ref', widget=OfficeTypeChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'} # TODO:  Unused but keep.  Filter by area?
        })),
        FieldPanel('state_judicial_district_office_ref', widget=StateJudicialDistrictOfficeChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'},
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

    template = 'campaigns/campaign_page.html'
    parent_page_types = ['campaigns.YearPage']
    subpage_types = []
    

    def save(self, *args, **kwargs):
        self.area_ref = self.district_ref
        self.office_ref = self.state_judicial_district_office_ref
        self.office_type_ref = self.office_ref.type_ref
        super().save(*args, **kwargs)
