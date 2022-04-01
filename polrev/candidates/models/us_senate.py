from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel, TabbedInterface, ObjectList

from .state import StateCandidatePageBase
from offices.widgets import UsSenateOfficeChooser

class UsSenateCandidatePage(StateCandidatePageBase):
    us_senate_office_ref = models.ForeignKey(
        'offices.UsSenateOffice',
        verbose_name=_('office'),
        on_delete=models.PROTECT,
        related_name='us_senate_candidates',
        null=True,
    )

    parent_page_types = ['candidates.CandidatesPage']
    subpage_types = []

    office_panels = StateCandidatePageBase.office_panels + [
            FieldPanel('us_senate_office_ref', widget=UsSenateOfficeChooser(linked_fields={
                'state_ref': {'id': 'id_state_ref'}
            })),
        ]

    edit_handler = TabbedInterface([
        ObjectList(StateCandidatePageBase.content_panels, heading='Content'),
        ObjectList(office_panels, heading='Office'),
        ObjectList(StateCandidatePageBase.promote_panels, heading='Promote'),
        ObjectList(StateCandidatePageBase.settings_panels, heading='Settings', classname="settings"),
    ])

    class Meta:
        verbose_name = "US Senate Candidate"

    def save(self, *args, **kwargs):
        self.area_ref = self.state_ref
        self.office_ref = self.us_senate_office_ref
        self.office_type_ref = self.office_ref.type_ref
        super().save(*args, **kwargs)
