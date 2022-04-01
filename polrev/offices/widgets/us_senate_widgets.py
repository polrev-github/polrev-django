from django.utils.translation import gettext_lazy as _

from generic_chooser.widgets import AdminChooser, LinkedFieldMixin

from offices.models import UsSenateOffice

class UsSenateOfficeChooser(LinkedFieldMixin, AdminChooser):
    #icon = 'user'
    model = UsSenateOffice
    page_title = _("Choose an office")
    choose_modal_url_name = 'us_senate_office_chooser:choose'