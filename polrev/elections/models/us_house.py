from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList

from .state import StateElectionPageBase

from areas.widgets.congressional_district_widgets import CongressionalDistrictChooser
from offices.widgets import UsHouseOfficeChooser

class UsHouseElectionPage(StateElectionPageBase):
    class Meta:
        verbose_name = "U.S. House Election"

    district_ref = models.ForeignKey(
        'areas.CongressionalDistrict',
        verbose_name=_('district'),
        on_delete=models.PROTECT,
        related_name='us_house_elections',
    )

    us_house_office_ref = models.ForeignKey(
        'offices.UsHouseOffice',
        verbose_name=_('office'),
        on_delete=models.PROTECT,
        related_name='us_house_elections',
        null=True,
    )

    office_panels = StateElectionPageBase.office_panels + [
        FieldPanel('district_ref', widget=CongressionalDistrictChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'}
        })),
        FieldPanel('us_house_office_ref', widget=UsHouseOfficeChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'},
            'district_ref': {'id': 'id_district_ref'},
            'office_type': {'title': 'U.S. House'}
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
        self.office_ref = self.us_house_office_ref
        self.office_type_ref = self.office_ref.type_ref
        super().save(*args, **kwargs)
