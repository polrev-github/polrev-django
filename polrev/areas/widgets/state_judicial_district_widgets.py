from django.utils.translation import gettext_lazy as _

from generic_chooser.widgets import AdminChooser, LinkedFieldMixin

from areas.models import StateJudicialDistrict


class StateJudicialDistrictChooser(LinkedFieldMixin, AdminChooser):
    # icon = 'user'
    model = StateJudicialDistrict
    page_title = _("Choose a district")
    choose_modal_url_name = "state_judicial_district_chooser:choose"
    is_searchable = True
