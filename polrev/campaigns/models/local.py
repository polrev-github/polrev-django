from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel, TabbedInterface, ObjectList

from .state import StateCampaignPageBase
from areas.widgets.place_widgets import PlaceChooser
from offices.widgets import OfficeTypeChooser, LocalOfficeChooser


class LocalCampaignPageBase(StateCampaignPageBase):

    place_ref = models.ForeignKey(
        'areas.Place',
        on_delete=models.PROTECT,
        related_name='local_campaigns',
    )

    office_panels = StateCampaignPageBase.office_panels + [
        FieldPanel('place_ref', widget=PlaceChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'}
        })),
    ]
    

class LocalCampaignPage(LocalCampaignPageBase):

    class Meta:
        verbose_name = "Local Campaign"

    local_office_ref = models.ForeignKey(
        'offices.LocalOffice',
        verbose_name=_('office'),
        on_delete=models.PROTECT,
        related_name='local_campaigns',
        null=True,
    )

    office_panels = LocalCampaignPageBase.office_panels + [
        FieldPanel('office_type_ref', widget=OfficeTypeChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'} # TODO:  Unused but keep.  Filter by area?
        })),
        FieldPanel('local_office_ref', widget=LocalOfficeChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'},
            'place_ref': {'id': 'id_place_ref'},
            'office_type_ref': {'id': 'id_office_type_ref'},
        })),
    ]

    edit_handler = TabbedInterface([
        ObjectList(StateCampaignPageBase.content_panels, heading='Content'),
        ObjectList(office_panels, heading='Office'),
        ObjectList(StateCampaignPageBase.promote_panels, heading='Promote'),
        ObjectList(StateCampaignPageBase.settings_panels, heading='Settings', classname="settings"),
    ])

    template = 'campaigns/campaign_page.html'
    parent_page_types = ['campaigns.YearPage']
    subpage_types = []

    def save(self, *args, **kwargs):
        self.area_ref = self.place_ref
        self.office_ref = self.local_office_ref
        super().save(*args, **kwargs)
