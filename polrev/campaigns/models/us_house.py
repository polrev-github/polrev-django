from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel, TabbedInterface, ObjectList

from .state import StateCampaignPageBase

from areas.widgets.congressional_district_widgets import CongressionalDistrictChooser
from offices.widgets import UsHouseOfficeChooser

class UsHouseCampaignPage(StateCampaignPageBase):
    class Meta:
        verbose_name = "U.S. House Campaign"

    district_ref = models.ForeignKey(
        'areas.CongressionalDistrict',
        verbose_name=_('district'),
        on_delete=models.PROTECT,
        related_name='us_house_campaigns',
    )

    us_house_office_ref = models.ForeignKey(
        'offices.UsHouseOffice',
        verbose_name=_('office'),
        on_delete=models.PROTECT,
        related_name='us_house_campaigns',
        null=True,
    )

    office_panels = StateCampaignPageBase.office_panels + [
        FieldPanel('district_ref', widget=CongressionalDistrictChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'}
        })),
        FieldPanel('us_house_office_ref', widget=UsHouseOfficeChooser(linked_fields={
            'state_ref': {'id': 'id_state_ref'},
            'district_ref': {'id': 'id_district_ref'},
            'office_type': {'title': 'U.S. House'}
        })),
    ]

    edit_handler = TabbedInterface([
        ObjectList(StateCampaignPageBase.content_panels, heading='Content'),
        ObjectList(office_panels, heading='Office'),
        ObjectList(StateCampaignPageBase.promote_panels, heading='Promote'),
        ObjectList(StateCampaignPageBase.settings_panels, heading='Settings', classname="settings"),
    ])

    parent_page_types = ['campaigns.YearPage']
    subpage_types = []
    
    def save(self, *args, **kwargs):
        self.area_ref = self.district_ref
        self.office_ref = self.us_house_office_ref
        self.office_type_ref = self.office_ref.type_ref
        super().save(*args, **kwargs)
