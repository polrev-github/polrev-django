from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

from wagtail.search import index

from model_utils.managers import InheritanceManager

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, PageChooserPanel


class Area(index.Indexed, models.Model):
    
    KIND_UNKNOWN = 0
    KIND_STATE = 1
    KIND_CONGRESSIONAL_DISTRICT = 1
    KIND_STATE_SENATE_DISTRICT = 2
    KIND_STATE_HOUSE_DISTRICT = 3
    KIND_COUNTY = 4

    # Places
    KIND_CITY = 5
    KIND_TOWN = 6
    KIND_VILLAGE = 7
    KIND_TOWNSHIP = 8
    KIND_CHARTER_TOWNSHIP = 9
    KIND_BOROUGH = 10
    KIND_CITY_BOROUGH = 11
    KIND_UNIFIED_GOVT = 12
    KIND_CONSOLIDATED_GOVT = 13
    KIND_METRO_GOVT = 14
    KIND_URBAN_COUNTY = 15
    KIND_CITY_COUNTY = 16
    KIND_MUNICIPALITY = 17
    KIND_CORPORATION = 18
    KIND_PLANTATION = 19

    KIND_COUNTY_COUNCIL_DISTRICT = 20
    KIND_LOCAL_COUNCIL_DISTRICT = 21

    # School Districts
    KIND_SD_UNIFIED = 22
    KIND_SD_ELEMENTARY = 23
    KIND_SD_SECONDARY = 24

    KIND_MAP = {
        KIND_UNKNOWN: 'Unknown',
        KIND_STATE: 'State',
        KIND_CONGRESSIONAL_DISTRICT: 'Congressional District',
        KIND_STATE_SENATE_DISTRICT: 'State Senate District',
        KIND_STATE_HOUSE_DISTRICT: 'State House District',
        KIND_COUNTY: 'County',
        # Places
        KIND_CITY: 'City',
        KIND_TOWN: 'Town',
        KIND_VILLAGE: 'Village',
        KIND_TOWNSHIP: 'Township',
        KIND_CHARTER_TOWNSHIP: 'Charter Township',
        KIND_BOROUGH: 'Borough',
        KIND_CITY_BOROUGH: 'City and Borough',
        KIND_UNIFIED_GOVT: 'Unified Government',
        KIND_CONSOLIDATED_GOVT: 'Consolidate Government',
        KIND_METRO_GOVT: 'Metropolitan Government',
        KIND_URBAN_COUNTY: 'Urban County',
        KIND_CITY_COUNTY: 'City and County',
        KIND_MUNICIPALITY: 'Municipality',
        KIND_CORPORATION: 'Corporation',
        KIND_PLANTATION: 'Plantation',
        # School Districts
        KIND_SD_UNIFIED: 'Unified School District',
        KIND_SD_ELEMENTARY: 'Elementary School District',
        KIND_SD_SECONDARY: 'Secondary School District'
    }

    KIND_CHOICES = list = [(k, v) for k, v in KIND_MAP.items()]

    class Meta:
        ordering = ['title']

    objects = InheritanceManager()

    kind = models.PositiveSmallIntegerField(choices=KIND_CHOICES, default=KIND_UNKNOWN)

    title = models.CharField(
        verbose_name=_('title'),
        max_length=256,
        help_text=_("Example: Mobile, Alabama")
    )

    name = models.CharField(
        verbose_name=_('name'),
        max_length=128,
        help_text=_("Example: United States, Alabama, Mobile")
    )

    state_fips = models.CharField(
        verbose_name=_('State FIPS Code'),
        max_length=2,
        help_text=_("Example: 01, 02 ... 50"),
        default='00'
    )

    gnis_feature_id = models.CharField(
        verbose_name=_('GNIS Feature Id'),
        max_length=8,
        help_text=_("Example: 01779775"),
        blank=True
    )
    
    panels = [
        #FieldPanel('title'),
        FieldPanel('name'),
        FieldPanel('state_fips'),
    ]

    search_fields = [
        index.SearchField('title', partial_match=True, boost=10),
    ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

