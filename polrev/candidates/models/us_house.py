from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel, TabbedInterface, ObjectList

from .state import StateCandidatePageBase

from areas.widgets import CongressionalDistrictChooser
from offices.widgets import UsHouseOfficeChooser

class UsHouseCandidatePage(StateCandidatePageBase):
    district_ref = models.ForeignKey(
        'areas.CongressionalDistrict',
        verbose_name=_('district'),
        on_delete=models.PROTECT,
        related_name='us_house_candidates',
    )

    us_house_office_ref = models.ForeignKey(
        'offices.UsHouseOffice',
        verbose_name=_('office'),
        on_delete=models.PROTECT,
        related_name='us_house_candidates',
        null=True,
    )

    office_panels = StateCandidatePageBase.office_panels + [
        FieldPanel('district_ref', widget=CongressionalDistrictChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'}
        })),
        FieldPanel('us_house_office_ref', widget=UsHouseOfficeChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'},
            'district_ref': {'id': 'id_district_ref'}
        })),
    ]

    edit_handler = TabbedInterface([
        ObjectList(StateCandidatePageBase.content_panels, heading='Content'),
        ObjectList(office_panels, heading='Office'),
        ObjectList(StateCandidatePageBase.promote_panels, heading='Promote'),
        ObjectList(StateCandidatePageBase.settings_panels, heading='Settings', classname="settings"),
    ])

    parent_page_types = ['candidates.CandidatesPage']
    subpage_types = []
    
    def save(self, *args, **kwargs):
        self.area_ref = self.district_ref
        self.office_ref = self.us_house_office_ref
        self.office_type_ref = self.office_ref.type_ref
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "US House Candidate"