from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.search import index
from wagtail.admin.panels import FieldPanel

from areas.models import Area


class CongressionalDistrict(Area):
    class Meta:
        ordering = ["cd_num"]

    state_ref = models.ForeignKey(
        "areas.State",
        verbose_name=_("State"),
        on_delete=models.PROTECT,
        related_name="congressional_districts",
    )

    cd_fips = models.CharField(
        verbose_name=_("Congressional District Code"),
        max_length=2,
        help_text=_("Example: 01 ... 99"),
    )
    cd_num = models.PositiveSmallIntegerField()

    panels = Area.panels + [
        FieldPanel("state_ref"),
        FieldPanel("cd_fips"),
    ]

    search_fields = Area.search_fields + [index.FilterField("state_ref_id")]

    def save(self, *args, **kwargs):
        self.kind = self.KIND_CONGRESSIONAL_DISTRICT
        self.state_fips = self.state_ref.state_fips
        self.title = f"{self.state_ref.name} {self.name}"
        self.cd_num = int(self.cd_fips)
        super().save(*args, **kwargs)
