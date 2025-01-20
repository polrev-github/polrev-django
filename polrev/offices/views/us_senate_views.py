from django.utils.translation import gettext_lazy as _

from generic_chooser.views import (
    ModelChooserMixin,
    ModelChooserCreateTabMixin,
    ModelChooserViewSet,
)

from offices.models import OfficeType, UsSenateOffice
from areas.models import State


class UsSenateOfficeChooserMixin(ModelChooserMixin):
    preserve_url_parameters = [
        "state_ref",
    ]  # preserve this URL parameter on pagination / search

    def get_unfiltered_object_list(self):
        objects = super().get_unfiltered_object_list()
        state_ref = self.request.GET.get("state_ref")
        if state_ref:
            objects = objects.filter(state_ref=state_ref)
        return objects


class UsSenateOfficeChooserCreateTabMixin(ModelChooserCreateTabMixin):
    def get_initial(self):
        data = self.initial.copy()
        state_ref = self.request.GET.get("state_ref")
        state = State.objects.get(id=state_ref)
        data["type_ref"] = OfficeType.TYPE_US_SENATE
        data["state_ref"] = state_ref
        data["title"] = f"U.S. Senate, {state.name}"
        return data


class UsSenateOfficeChooserViewSet(ModelChooserViewSet):
    chooser_mixin_class = UsSenateOfficeChooserMixin
    create_tab_mixin_class = UsSenateOfficeChooserCreateTabMixin
    # icon = 'user'
    model = UsSenateOffice
    page_title = _("Choose an office")
    per_page = 10
    order_by = "title"
    fields = ["type_ref", "state_ref", "title", "website"]
