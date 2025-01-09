from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList

from .state import StateElectionPageBase
from areas.widgets.legislate_district_widgets import StateHouseDistrictChooser
from offices.widgets import StateHouseOfficeChooser

class StateHouseElectionPage(StateElectionPageBase):

    class Meta:
        verbose_name = "State House Election"

    district_ref = models.ForeignKey(
        'areas.StateHouseDistrict',
        on_delete=models.PROTECT,
        related_name='state_house_elections',
    )

    state_house_office_ref = models.ForeignKey(
        'offices.StateHouseOffice',
        verbose_name=_('office'),
        on_delete=models.PROTECT,
        related_name='state_house_elections',
        null=True,
    )

    office_panels = StateElectionPageBase.office_panels + [
        FieldPanel('district_ref', widget=StateHouseDistrictChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'}
        })),
        FieldPanel('state_house_office_ref', widget=StateHouseOfficeChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'},
            'district_ref': {'id': 'id_district_ref'},
            'office_type': {'title': 'State House'}
        })),
    ]

    edit_handler = TabbedInterface([
        ObjectList(StateElectionPageBase.content_panels, heading='Content'),
        ObjectList(office_panels, heading='Office'),
        ObjectList(StateElectionPageBase.promote_panels, heading='Promote'),
        ObjectList(StateElectionPageBase.settings_panels, heading='Settings', classname="settings"),
    ])

    template = 'elections/election_page.html'
    parent_page_types = ['elections.YearPage']
    subpage_types = []
    

    def save(self, *args, **kwargs):
        self.area_ref = self.district_ref
        self.office_ref = self.state_house_office_ref
        self.office_type_ref = self.office_ref.type_ref
        super().save(*args, **kwargs)
