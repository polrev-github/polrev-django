from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel, TabbedInterface, ObjectList

from .state import StateCandidatePageBase
from areas.widgets import StateSenateDistrictChooser
from offices.widgets import StateSenateOfficeChooser

class StateSenateCandidatePage(StateCandidatePageBase):

    class Meta:
        verbose_name = "State Senate Candidate"

    district_ref = models.ForeignKey(
        'areas.StateSenateDistrict',
        verbose_name=_('district'),
        on_delete=models.PROTECT,
        related_name='state_senate_candidates',
    )

    state_senate_office_ref = models.ForeignKey(
        'offices.StateSenateOffice',
        verbose_name=_('office'),
        on_delete=models.PROTECT,
        related_name='state_senate_candidates',
        null=True,
    )

    office_panels = StateCandidatePageBase.office_panels + [
        FieldPanel('district_ref', widget=StateSenateDistrictChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'}
        })),
        FieldPanel('state_senate_office_ref', widget=StateSenateOfficeChooser(linked_fields={
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
        self.office_ref = self.state_senate_office_ref
        self.office_type_ref = self.office_ref.type_ref
        super().save(*args, **kwargs)
