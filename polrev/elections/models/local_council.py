from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList

from .local import LocalElectionPageBase
from areas.widgets.place_widgets import PlaceChooser
from areas.widgets.local_council_district_widgets import LocalCouncilDistrictChooser
from offices.widgets import OfficeTypeChooser, LocalCouncilOfficeChooser

class LocalCouncilElectionPage(LocalElectionPageBase):

    class Meta:
        verbose_name = "Local Council Election"

    district_ref = models.ForeignKey(
        'areas.LocalCouncilDistrict',
        verbose_name=_('district'),
        on_delete=models.PROTECT,
        related_name='local_council_elections',
    )

    local_council_office_ref = models.ForeignKey(
        'offices.LocalCouncilOffice',
        verbose_name=_('office'),
        on_delete=models.PROTECT,
        related_name='local_council_elections',
        null=True,
    )

    office_panels = LocalElectionPageBase.office_panels + [
        FieldPanel('district_ref', widget=LocalCouncilDistrictChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'},
            'place_ref': {'id': 'id_place_ref'}
        })),
        FieldPanel('office_type_ref', widget=OfficeTypeChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'} # TODO:  Unused but keep.  Filter by area?
        })),
        FieldPanel('local_council_office_ref', widget=LocalCouncilOfficeChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'},
            'place_ref': {'id': 'id_place_ref'},
            'district_ref': {'id': 'id_district_ref'},
            'office_type_ref': {'id': 'id_office_type_ref'},
            'office_type': {'title': 'City Council'}
        })),
    ]

    edit_handler = TabbedInterface([
        ObjectList(LocalElectionPageBase.content_panels, heading='Content'),
        ObjectList(office_panels, heading='Office'),
        ObjectList(LocalElectionPageBase.promote_panels, heading='Promote'),
        ObjectList(LocalElectionPageBase.settings_panels, heading='Settings', classname="settings"),
    ])

    template = 'elections/election_page.html'
    parent_page_types = ['elections.YearPage']
    subpage_types = []
    

    def save(self, *args, **kwargs):
        self.area_ref = self.district_ref
        self.office_ref = self.local_council_office_ref
        super().save(*args, **kwargs)
