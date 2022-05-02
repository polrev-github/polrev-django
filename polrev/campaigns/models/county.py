from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel, TabbedInterface, ObjectList

from .state import StateCampaignPageBase
from areas.widgets.county_widgets import CountyChooser
from offices.widgets import OfficeTypeChooser, CountyOfficeChooser


class CountyCampaignPageBase(StateCampaignPageBase):

    county_ref = models.ForeignKey(
        'areas.County',
        verbose_name=_('county'),
        on_delete=models.PROTECT,
        related_name='county_campaigns',
    )

    office_panels = StateCampaignPageBase.office_panels + [
        FieldPanel('county_ref', widget=CountyChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'}
        })),
    ]

    parent_page_types = ['campaigns.YearPage']
    subpage_types = []


class CountyCampaignPage(CountyCampaignPageBase):

    class Meta:
        verbose_name = "County Campaign"

    county_office_ref = models.ForeignKey(
        'offices.CountyOffice',
        verbose_name=_('office'),
        on_delete=models.PROTECT,
        related_name='county_campaigns',
        null=True,
    )

    office_panels = CountyCampaignPageBase.office_panels + [
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
        ObjectList(StateCampaignPageBase.content_panels, heading='Content'),
        ObjectList(office_panels, heading='Office'),
        ObjectList(StateCampaignPageBase.promote_panels, heading='Promote'),
        ObjectList(StateCampaignPageBase.settings_panels, heading='Settings', classname="settings"),
    ])

    template = 'campaigns/campaign_page.html'
    parent_page_types = ['campaigns.YearPage']
    subpage_types = []
    

    def save(self, *args, **kwargs):
        self.area_ref = self.county_ref
        self.office_ref = self.county_office_ref
        super().save(*args, **kwargs)
