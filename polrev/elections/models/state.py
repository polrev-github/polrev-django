from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList

from .election import ElectionPage

from offices.widgets import OfficeTypeChooser, StateOfficeChooser

class StateElectionPageBase(ElectionPage):
    state_ref = models.ForeignKey(
        'areas.State',
        verbose_name=_('state'),
        on_delete=models.PROTECT,
        related_name='state_elections',
    )

    office_panels =  [
        FieldPanel('state_ref'),
    ] + ElectionPage.office_panels

    def save(self, *args, **kwargs):
        self.state_fips = self.state_ref.state_fips
        super().save(*args, **kwargs)


class StateElectionPage(StateElectionPageBase):

    class Meta:
        verbose_name = "State Election"

    state_office_ref = models.ForeignKey(
        'offices.StateOfficeBase',
        verbose_name=_('office'),
        on_delete=models.PROTECT,
        related_name='state_elections',
        null=True,
    )

    office_panels = StateElectionPageBase.office_panels + [
        FieldPanel('office_type_ref', widget=OfficeTypeChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'} # TODO:  Unused but keep.  Filter by area?
        })),
        FieldPanel('state_office_ref', widget=StateOfficeChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'},
            'office_type_ref': {'id': 'id_office_type_ref'},
        })),
    ]

    edit_handler = TabbedInterface([
        ObjectList(ElectionPage.content_panels, heading='Content'),
        ObjectList(office_panels, heading='Office'),
        ObjectList(ElectionPage.promote_panels, heading='Promote'),
        ObjectList(ElectionPage.settings_panels, heading='Settings', classname="settings"),
    ])

    template = 'elections/election_page.html'
    parent_page_types = ['elections.YearPage']
    subpage_types = []

    def save(self, *args, **kwargs):
        self.area_ref = self.state_ref
        self.office_ref = self.state_office_ref
        super().save(*args, **kwargs)
