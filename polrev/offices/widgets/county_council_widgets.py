from django.utils.translation import gettext_lazy as _

from generic_chooser.widgets import AdminChooser, LinkedFieldMixin

from offices.models import CountyCouncilOffice


class CountyCouncilOfficeChooser(LinkedFieldMixin, AdminChooser):
    # icon = 'user'
    model = CountyCouncilOffice
    page_title = _("Choose an office")
    choose_modal_url_name = "county_council_office_chooser:choose"
