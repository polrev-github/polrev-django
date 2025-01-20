from django.utils.translation import gettext_lazy as _

from generic_chooser.widgets import AdminChooser, LinkedFieldMixin

from areas.models import SchoolDistrict


class SchoolDistrictChooser(LinkedFieldMixin, AdminChooser):
    # icon = 'user'
    model = SchoolDistrict
    page_title = _("Choose a district")
    choose_modal_url_name = "school_district_chooser:choose"
    is_searchable = True
