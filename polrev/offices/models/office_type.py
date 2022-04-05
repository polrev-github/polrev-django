from django.db import models
from django.utils.translation import ugettext_lazy as _

class OfficeType(models.Model):
    TYPE_US_SENATE = 1
    TYPE_US_HOUSE = 2
    TYPE_STATE_SENATE = 3
    TYPE_STATE_HOUSE = 4
    
    class Meta:
        ordering = ['title']

    title = models.CharField(
        verbose_name=_('title'),
        max_length=256,
        help_text=_("Example: U.S. Senate, State House, Mayor, City Council")
    )

    def __str__(self):
        return self.title
