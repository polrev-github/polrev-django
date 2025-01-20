from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.panels import FieldPanel

from .office import Office


class StateOfficeBase(Office):
    state_ref = models.ForeignKey(
        "areas.State",
        verbose_name=_("state"),
        on_delete=models.PROTECT,
        related_name="state_offices",
    )

    area_panels = Office.area_panels + [
        FieldPanel("state_ref"),
    ]

    def save(self, *args, **kwargs):
        self.state_fips = self.state_ref.state_fips
        self.title = f"{self.type_ref.title}, {self.area_ref.title}"
        super().save(*args, **kwargs)


class StateOffice(StateOfficeBase):

    class Meta:
        verbose_name = "State Office"

    panels = StateOfficeBase.area_panels + Office.other_panels

    def save(self, *args, **kwargs):
        self.area_ref = self.state_ref
        super().save(*args, **kwargs)
