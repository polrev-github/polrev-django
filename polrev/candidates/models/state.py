from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel, TabbedInterface, ObjectList

from .candidate import CandidatePage

from offices.widgets import OfficeTypeChooser, StateOfficeChooser

class StateCandidatePageBase(CandidatePage):
    state_ref = models.ForeignKey(
        'areas.State',
        verbose_name=_('state'),
        on_delete=models.PROTECT,
        related_name='state_candidates',
    )

    office_panels =  [
        FieldPanel('state_ref'),
    ] + CandidatePage.office_panels

    def save(self, *args, **kwargs):
        self.state_fips = self.state_ref.state_fips
        super().save(*args, **kwargs)


class StateCandidatePage(StateCandidatePageBase):

    class Meta:
        verbose_name = "State Candidate"

    state_office_ref = models.ForeignKey(
        'offices.StateOfficeBase',
        verbose_name=_('office'),
        on_delete=models.PROTECT,
        related_name='state_candidates',
        null=True,
    )

    office_panels = StateCandidatePageBase.office_panels + [
        FieldPanel('office_type_ref', widget=OfficeTypeChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'} # TODO:  Unused but keep.  Filter by area?
        })),
        FieldPanel('state_office_ref', widget=StateOfficeChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'},
            'office_type_ref': {'id': 'id_office_type_ref'},
        })),
    ]

    edit_handler = TabbedInterface([
        ObjectList(CandidatePage.content_panels, heading='Content'),
        ObjectList(office_panels, heading='Office'),
        ObjectList(CandidatePage.promote_panels, heading='Promote'),
        ObjectList(CandidatePage.settings_panels, heading='Settings', classname="settings"),
    ])

    parent_page_types = ['candidates.CandidatesPage']
    subpage_types = []

    def save(self, *args, **kwargs):
        self.area_ref = self.state_ref
        self.office_ref = self.state_office_ref
        super().save(*args, **kwargs)
