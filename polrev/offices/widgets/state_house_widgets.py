from django.utils.translation import gettext_lazy as _

from generic_chooser.widgets import AdminChooser, LinkedFieldMixin

from offices.models import StateHouseOffice

class StateHouseOfficeChooser(LinkedFieldMixin, AdminChooser):
    #icon = 'user'
    model = StateHouseOffice
    page_title = _("Choose an office")
    choose_modal_url_name = 'state_house_office_chooser:choose'