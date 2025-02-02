from django.utils.translation import gettext_lazy as _

from generic_chooser.widgets import AdminChooser, LinkedFieldMixin

from offices.models import UsHouseOffice


class UsHouseOfficeChooser(LinkedFieldMixin, AdminChooser):
    # icon = 'user'
    model = UsHouseOffice
    page_title = _("Choose an office")
    choose_modal_url_name = "us_house_office_chooser:choose"
