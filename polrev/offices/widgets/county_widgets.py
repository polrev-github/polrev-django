from django.utils.translation import gettext_lazy as _

from generic_chooser.widgets import AdminChooser, LinkedFieldMixin

from offices.models import CountyOffice


class CountyOfficeChooser(LinkedFieldMixin, AdminChooser):
    # icon = 'user'
    model = CountyOffice
    page_title = _("Choose an office")
    choose_modal_url_name = "county_office_chooser:choose"
