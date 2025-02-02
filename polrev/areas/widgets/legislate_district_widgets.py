from django.utils.translation import gettext_lazy as _

from generic_chooser.widgets import AdminChooser, LinkedFieldMixin

from areas.models import StateSenateDistrict, StateHouseDistrict


class StateSenateDistrictChooser(LinkedFieldMixin, AdminChooser):
    # icon = 'user'
    model = StateSenateDistrict
    page_title = _("Choose a district")
    choose_modal_url_name = "state_senate_district_chooser:choose"


class StateHouseDistrictChooser(LinkedFieldMixin, AdminChooser):
    # icon = 'user'
    model = StateHouseDistrict
    page_title = _("Choose a district")
    choose_modal_url_name = "state_house_district_chooser:choose"
