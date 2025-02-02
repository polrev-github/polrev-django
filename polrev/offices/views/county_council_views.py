from django.utils.translation import gettext_lazy as _

from generic_chooser.views import (
    ModelChooserMixin,
    ModelChooserCreateTabMixin,
    ModelChooserViewSet,
)

from offices.models import OfficeType, CountyCouncilOffice
from areas.models import CountyCouncilDistrict


class CountyCouncilOfficeChooserMixin(ModelChooserMixin):
    preserve_url_parameters = [
        "state_ref",
        "county_ref",
        "district_ref",
        "office_type_ref",
    ]

    def get_unfiltered_object_list(self):
        objects = super().get_unfiltered_object_list()
        county_ref = self.request.GET.get("county_ref")
        if county_ref:
            objects = objects.filter(county_ref=county_ref)
        return objects


class CountyCouncilOfficeChooserCreateTabMixin(ModelChooserCreateTabMixin):
    def get_initial(self):
        data = self.initial.copy()
        state_ref = self.request.GET.get("state_ref")
        county_ref = self.request.GET.get("county_ref")
        district_ref = self.request.GET.get("district_ref")
        type_ref = self.request.GET.get("office_type_ref")

        district = CountyCouncilDistrict.objects.get(id=district_ref)
        data["state_ref"] = state_ref
        data["county_ref"] = county_ref
        data["district_ref"] = district_ref
        data["type_ref"] = type_ref
        office_type = OfficeType.objects.get(id=type_ref)
        data["title"] = f"{office_type.title}, {district.title}"
        return data


class CountyCouncilOfficeChooserViewSet(ModelChooserViewSet):
    chooser_mixin_class = CountyCouncilOfficeChooserMixin
    create_tab_mixin_class = CountyCouncilOfficeChooserCreateTabMixin
    icon = "user"
    model = CountyCouncilOffice
    page_title = _("Choose an office")
    per_page = 10
    fields = ["type_ref", "state_ref", "county_ref", "district_ref", "title", "website"]
