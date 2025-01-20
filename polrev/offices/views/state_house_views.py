from django.utils.translation import gettext_lazy as _

from generic_chooser.views import (
    ModelChooserMixin,
    ModelChooserCreateTabMixin,
    ModelChooserViewSet,
)

from offices.models import OfficeType, StateHouseOffice
from areas.models import StateHouseDistrict


class StateHouseOfficeChooserMixin(ModelChooserMixin):
    preserve_url_parameters = [
        "district_ref",
    ]  # preserve this URL parameter on pagination / search

    def get_unfiltered_object_list(self):
        objects = super().get_unfiltered_object_list()
        district_ref = self.request.GET.get("district_ref")
        if district_ref:
            objects = objects.filter(district_ref=district_ref)
        return objects


class StateHouseOfficeChooserCreateTabMixin(ModelChooserCreateTabMixin):
    def get_initial(self):
        data = self.initial.copy()
        state_ref = self.request.GET.get("state_ref")
        district_ref = self.request.GET.get("district_ref")

        district = StateHouseDistrict.objects.get(id=district_ref)
        data["type_ref"] = OfficeType.TYPE_STATE_HOUSE
        data["state_ref"] = state_ref
        data["district_ref"] = district_ref
        data["title"] = f"State House, {district.title}"
        data["number"] = district.district_num
        return data


class StateHouseOfficeChooserViewSet(ModelChooserViewSet):
    chooser_mixin_class = StateHouseOfficeChooserMixin
    create_tab_mixin_class = StateHouseOfficeChooserCreateTabMixin
    icon = "user"
    model = StateHouseOffice
    page_title = _("Choose an office")
    per_page = 10
    # order_by = 'title'
    fields = ["type_ref", "state_ref", "district_ref", "title", "number", "website"]
