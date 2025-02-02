from django.utils.translation import gettext_lazy as _

from generic_chooser.widgets import AdminChooser, LinkedFieldMixin

from offices.models import StateSenateOffice


class StateSenateOfficeChooser(LinkedFieldMixin, AdminChooser):
    # icon = 'user'
    model = StateSenateOffice
    page_title = _("Choose a district")
    choose_modal_url_name = "state_senate_office_chooser:choose"
