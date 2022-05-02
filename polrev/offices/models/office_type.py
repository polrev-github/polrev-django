from django.db import models
from django.utils.translation import ugettext_lazy as _
from wagtail.search import index

class OfficeType(index.Indexed, models.Model):
    TYPE_US_SENATE = 1
    TYPE_US_HOUSE = 2
    TYPE_STATE_SENATE = 3
    TYPE_STATE_HOUSE = 4
    
    class Meta:
        ordering = ['rank']

    title = models.CharField(
        verbose_name=_('title'),
        max_length=256,
        help_text=_("Example: U.S. Senate, State House, Mayor, City Council")
    )

    rank = models.PositiveSmallIntegerField(
        default=1000,
        help_text=_("Sorting priority.  Example: 0, 100, etc")
    )

    search_fields = [
        index.SearchField('title', partial_match=True, boost=10),
    ]

    def __str__(self):
        return self.title
