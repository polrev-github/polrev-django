from django.utils.translation import gettext_lazy as _

from generic_chooser.widgets import AdminChooser, LinkedFieldMixin

from offices.models import LocalCouncilOffice

class LocalCouncilOfficeChooser(LinkedFieldMixin, AdminChooser):
    #icon = 'user'
    model = LocalCouncilOffice
    page_title = _("Choose an office")
    choose_modal_url_name = 'local_council_office_chooser:choose'