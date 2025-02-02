from django.utils.translation import gettext_lazy as _

from generic_chooser.widgets import AdminChooser, LinkedFieldMixin

from offices.models import SchoolDistrictOffice


class SchoolDistrictOfficeChooser(LinkedFieldMixin, AdminChooser):
    # icon = 'user'
    model = SchoolDistrictOffice
    page_title = _("Choose an office")
    choose_modal_url_name = "school_district_office_chooser:choose"
