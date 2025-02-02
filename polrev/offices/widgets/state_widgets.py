from django.utils.translation import gettext_lazy as _

from generic_chooser.widgets import AdminChooser, LinkedFieldMixin

from offices.models import StateOffice


class StateOfficeChooser(LinkedFieldMixin, AdminChooser):
    # icon = 'user'
    model = StateOffice
    page_title = _("Choose an office")
    choose_modal_url_name = "state_office_chooser:choose"
