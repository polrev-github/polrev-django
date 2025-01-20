from django.db import models

from django.utils.translation import gettext_lazy as _

from wagtail.search import index
from wagtail.admin.panels import FieldPanel


from areas.models import Area


class County(Area):
    class Meta:
        verbose_name_plural = "counties"

    state_ref = models.ForeignKey(
        "areas.State",
        verbose_name=_("State"),
        on_delete=models.PROTECT,
        related_name="counties",
    )

    county_fips = models.CharField(
        verbose_name=_("County FIPS Code"),
        max_length=3,
        help_text=_("Example: 001, 002 ..."),
    )

    class_fips = models.CharField(
        verbose_name=_("County Class FIPS Code"),
        max_length=2,
        help_text=_("Example: H1, H4 ..."),
    )

    panels = Area.panels + [
        FieldPanel("state_ref"),
        FieldPanel("county_fips"),
        FieldPanel("class_fips"),
    ]

    search_fields = Area.search_fields + [index.FilterField("state_ref_id")]

    def save(self, *args, **kwargs):
        self.kind = self.KIND_COUNTY
        self.state_fips = self.state_ref.state_fips
        self.title = f"{self.name}, {self.state_ref.name}"
        super().save(*args, **kwargs)
