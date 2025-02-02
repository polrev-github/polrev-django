from django.utils.translation import gettext_lazy as _

from generic_chooser.widgets import AdminChooser, LinkedFieldMixin

from offices.models import LocalOffice


class LocalOfficeChooser(LinkedFieldMixin, AdminChooser):
    # icon = 'user'
    model = LocalOffice
    page_title = _("Choose an office")
    choose_modal_url_name = "local_office_chooser:choose"
