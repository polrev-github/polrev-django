from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList

from .campaign import CampaignPage

from offices.widgets import OfficeTypeChooser, StateOfficeChooser

class StateCampaignPageBase(CampaignPage):
    state_ref = models.ForeignKey(
        'areas.State',
        verbose_name=_('state'),
        on_delete=models.PROTECT,
        related_name='state_campaigns',
    )

    office_panels =  [
        FieldPanel('state_ref'),
    ] + CampaignPage.office_panels

    def save(self, *args, **kwargs):
        self.state_fips = self.state_ref.state_fips
        super().save(*args, **kwargs)


class StateCampaignPage(StateCampaignPageBase):

    class Meta:
        verbose_name = "State Campaign"

    state_office_ref = models.ForeignKey(
        'offices.StateOfficeBase',
        verbose_name=_('office'),
        on_delete=models.PROTECT,
        related_name='state_campaigns',
        null=True,
    )

    office_panels = StateCampaignPageBase.office_panels + [
        FieldPanel('office_type_ref', widget=OfficeTypeChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'} # TODO:  Unused but keep.  Filter by area?
        })),
        FieldPanel('state_office_ref', widget=StateOfficeChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'},
            'office_type_ref': {'id': 'id_office_type_ref'},
        })),
    ]

    edit_handler = TabbedInterface([
        ObjectList(CampaignPage.content_panels, heading='Content'),
        ObjectList(office_panels, heading='Office'),
        ObjectList(CampaignPage.promote_panels, heading='Promote'),
        ObjectList(CampaignPage.settings_panels, heading='Settings', classname="settings"),
    ])

    template = 'campaigns/campaign_page.html'
    parent_page_types = ['campaigns.YearPage']
    subpage_types = []

    def save(self, *args, **kwargs):
        self.area_ref = self.state_ref
        self.office_ref = self.state_office_ref
        super().save(*args, **kwargs)
