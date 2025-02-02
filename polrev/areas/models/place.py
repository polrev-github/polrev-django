from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.panels import FieldPanel
from wagtail.search import index


from areas.models import Area


class Place(Area):
    state_ref = models.ForeignKey(
        "areas.State",
        verbose_name=_("State"),
        on_delete=models.PROTECT,
        related_name="places",
    )

    counties = models.ManyToManyField("areas.County")

    place_fips = models.CharField(
        verbose_name=_("Place FIPS Code"), max_length=5, help_text=_("Example: 00123")
    )

    panels = Area.panels + [
        FieldPanel("state_ref"),
        FieldPanel("place_fips"),
        FieldPanel("counties"),
    ]

    search_fields = Area.search_fields + [
        index.FilterField("state_ref_id"),
    ]

    def save(self, *args, **kwargs):
        self.state_fips = self.state_ref.state_fips
        self.title = f"{self.name}, {self.state_ref.name}"
        super().save(*args, **kwargs)
