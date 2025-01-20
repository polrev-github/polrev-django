from .state import StateOfficeBase


class UsSenateOffice(StateOfficeBase):

    class Meta:
        verbose_name = "US Senate Office"

    def save(self, *args, **kwargs):
        self.area_ref = self.state_ref
        super().save(*args, **kwargs)
