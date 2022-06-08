from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel, TabbedInterface, ObjectList

from .state import StateElectionPageBase
from offices.widgets import UsSenateOfficeChooser

class UsSenateElectionPage(StateElectionPageBase):
    class Meta:
        verbose_name = "U.S. Senate Election"

    us_senate_office_ref = models.ForeignKey(
        'offices.UsSenateOffice',
        verbose_name=_('office'),
        on_delete=models.PROTECT,
        related_name='us_senate_elections',
        null=True,
    )

    template = 'elections/election_page.html'
    parent_page_types = ['elections.YearPage']
    subpage_types = []

    office_panels = StateElectionPageBase.office_panels + [
            FieldPanel('us_senate_office_ref', widget=UsSenateOfficeChooser(linked_fields={
                'state_ref': {'id': 'id_state_ref'},
                'office_type': {'title': 'U.S. Senate'}
            })),
        ]

    edit_handler = TabbedInterface([
        ObjectList(StateElectionPageBase.content_panels, heading='Content'),
        ObjectList(office_panels, heading='Office'),
        ObjectList(StateElectionPageBase.promote_panels, heading='Promote'),
        ObjectList(StateElectionPageBase.settings_panels, heading='Settings', classname="settings"),
    ])

    def save(self, *args, **kwargs):
        self.area_ref = self.state_ref
        self.office_ref = self.us_senate_office_ref
        self.office_type_ref = self.office_ref.type_ref
        super().save(*args, **kwargs)
