from django.utils.translation import gettext_lazy as _

from generic_chooser.views import (
    ModelChooserMixin,
    ModelChooserCreateTabMixin,
    ModelChooserViewSet,
)

from offices.models import OfficeType, LocalOffice
from offices.forms import LocalOfficeForm
from areas.models import Place


class LocalOfficeChooserMixin(ModelChooserMixin):
    preserve_url_parameters = ["state_ref", "place_ref", "office_type_ref"]

    def get_unfiltered_object_list(self):
        objects = super().get_unfiltered_object_list()
        place_ref = self.request.GET.get("place_ref")
        if place_ref:
            objects = objects.filter(place_ref=place_ref)
        return objects


class LocalOfficeChooserCreateTabMixin(ModelChooserCreateTabMixin):
    def get_initial(self):
        data = self.initial.copy()
        state_ref = self.request.GET.get("state_ref")
        place_ref = self.request.GET.get("place_ref")
        type_ref = self.request.GET.get("office_type_ref")

        place = Place.objects.get(id=place_ref)
        data["state_ref"] = state_ref
        data["place_ref"] = place_ref
        data["type_ref"] = type_ref
        office_type = OfficeType.objects.get(id=type_ref)
        data["title"] = f"{office_type.title}, {place.title}"
        return data


class LocalOfficeChooserViewSet(ModelChooserViewSet):
    chooser_mixin_class = LocalOfficeChooserMixin
    create_tab_mixin_class = LocalOfficeChooserCreateTabMixin
    form_class = LocalOfficeForm
    icon = "user"
    model = LocalOffice
    page_title = _("Choose an office")
    per_page = 10
    fields = ["type_ref", "state_ref", "place_ref", "title", "website"]
