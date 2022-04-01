from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel, TabbedInterface, ObjectList

from .state import StateCandidatePageBase
from areas.widgets import CountyChooser
from areas.widgets.county_council_district_widgets import CountyCouncilDistrictChooser
from offices.widgets import OfficeTypeChooser, CountyCouncilOfficeChooser

class CountyCouncilCandidatePage(StateCandidatePageBase):

    class Meta:
        verbose_name = "County Council Candidate"

    county_ref = models.ForeignKey(
        'areas.County',
        verbose_name=_('county'),
        on_delete=models.PROTECT,
        related_name='county_council_candidates',
    )

    district_ref = models.ForeignKey(
        'areas.CountyCouncilDistrict',
        verbose_name=_('district'),
        on_delete=models.PROTECT,
        related_name='county_council_candidates',
    )

    county_council_office_ref = models.ForeignKey(
        'offices.CountyCouncilOffice',
        verbose_name=_('office'),
        on_delete=models.PROTECT,
        related_name='county_council_candidates',
        null=True,
    )

    office_panels = StateCandidatePageBase.office_panels + [
        FieldPanel('county_ref', widget=CountyChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'}
        })),
        FieldPanel('district_ref', widget=CountyCouncilDistrictChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'},
            'county_ref': {'id': 'id_county_ref'}
        })),
        FieldPanel('office_type_ref', widget=OfficeTypeChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'} # TODO:  Unused but keep.  Filter by area?
        })),
        FieldPanel('county_council_office_ref', widget=CountyCouncilOfficeChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'},
            'county_ref': {'id': 'id_county_ref'},
            'district_ref': {'id': 'id_district_ref'},
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
        self.area_ref = self.district_ref
        self.office_ref = self.county_council_office_ref
        super().save(*args, **kwargs)
