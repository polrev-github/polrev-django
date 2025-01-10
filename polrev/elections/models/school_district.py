from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList

from .state import StateElectionPageBase
from areas.widgets.school_district_widgets import SchoolDistrictChooser
from offices.widgets import OfficeTypeChooser, SchoolDistrictOfficeChooser

class SchoolDistrictElectionPage(StateElectionPageBase):

    class Meta:
        verbose_name = "School District Election"

    district_ref = models.ForeignKey(
        'areas.SchoolDistrict',
        on_delete=models.PROTECT,
        related_name='school_district_elections',
    )

    school_district_office_ref = models.ForeignKey(
        'offices.SchoolDistrictOffice',
        verbose_name=_('office'),
        on_delete=models.PROTECT,
        related_name='school_district_elections',
        null=True,
    )

    office_panels = StateElectionPageBase.office_panels + [
        FieldPanel('district_ref', widget=SchoolDistrictChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'}
        })),
        FieldPanel('office_type_ref', widget=OfficeTypeChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'} # TODO:  Unused but keep.  Filter by area?
        })),
        FieldPanel('school_district_office_ref', widget=SchoolDistrictOfficeChooser(linked_fields={
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
        self.office_ref = self.school_district_office_ref
        super().save(*args, **kwargs)
