from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel, TabbedInterface, ObjectList

from .state import StateCandidatePageBase
from areas.widgets import CountyChooser
from offices.widgets import OfficeTypeChooser, CountyOfficeChooser

class CountyCandidatePage(StateCandidatePageBase):

    class Meta:
        verbose_name = "County Candidate"

    county_ref = models.ForeignKey(
        'areas.County',
        verbose_name=_('county'),
        on_delete=models.PROTECT,
        related_name='county_candidates',
    )

    county_office_ref = models.ForeignKey(
        'offices.CountyOffice',
        verbose_name=_('office'),
        on_delete=models.PROTECT,
        related_name='county_candidates',
        null=True,
    )

    office_panels = StateCandidatePageBase.office_panels + [
        FieldPanel('county_ref', widget=CountyChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'}
        })),
        FieldPanel('office_type_ref', widget=OfficeTypeChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'} # TODO:  Unused but keep.  Filter by area?
        })),
        FieldPanel('county_office_ref', widget=CountyOfficeChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'},
            'county_ref': {'id': 'id_county_ref'},
            'office_type_ref': {'id': 'id_office_type_ref'},
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
        self.area_ref = self.county_ref
        self.office_ref = self.county_office_ref
        super().save(*args, **kwargs)
