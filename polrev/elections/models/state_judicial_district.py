from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel, TabbedInterface, ObjectList

from .state import StateElectionPageBase
from areas.widgets.state_judicial_district_widgets import StateJudicialDistrictChooser
from offices.widgets import OfficeTypeChooser, StateJudicialDistrictOfficeChooser

class StateJudicialDistrictElectionPage(StateElectionPageBase):

    class Meta:
        verbose_name = "State Judicial District Election"

    district_ref = models.ForeignKey(
        'areas.StateJudicialDistrict',
        on_delete=models.PROTECT,
        related_name='state_judicial_district_elections',
    )

    state_judicial_district_office_ref = models.ForeignKey(
        'offices.StateJudicialDistrictOffice',
        verbose_name=_('office'),
        on_delete=models.PROTECT,
        related_name='state_judicial_district_elections',
        null=True,
    )

    office_panels = StateElectionPageBase.office_panels + [
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
        self.office_ref = self.state_judicial_district_office_ref
        self.office_type_ref = self.office_ref.type_ref
        super().save(*args, **kwargs)
