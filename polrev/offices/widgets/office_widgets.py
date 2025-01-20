from django.utils.translation import gettext_lazy as _

from generic_chooser.widgets import AdminChooser, LinkedFieldMixin

from offices.models import OfficeType


class OfficeTypeChooser(LinkedFieldMixin, AdminChooser):
    # icon = 'user'
    model = OfficeType
    page_title = _("Choose an office")
    choose_modal_url_name = "office_type_chooser:choose"
