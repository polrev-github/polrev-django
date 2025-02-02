from django.utils.translation import gettext_lazy as _

from generic_chooser.widgets import AdminChooser, LinkedFieldMixin

from areas.models import Place


class PlaceChooser(LinkedFieldMixin, AdminChooser):
    # icon = 'user'
    model = Place
    page_title = _("Choose a place")
    choose_modal_url_name = "place_chooser:choose"
    is_searchable = True
