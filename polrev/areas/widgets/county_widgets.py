from django.utils.translation import gettext_lazy as _

from generic_chooser.widgets import AdminChooser, LinkedFieldMixin

from areas.models import County


class CountyChooser(LinkedFieldMixin, AdminChooser):
    # icon = 'user'
    model = County
    page_title = _("Choose a county")
    choose_modal_url_name = "county_chooser:choose"
