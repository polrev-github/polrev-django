from django.utils.translation import gettext_lazy as _

from generic_chooser.widgets import AdminChooser, LinkedFieldMixin

from areas.models import CountyJudicialPrecinct

#TODO: Why isn't this being used?

class CountyJudicialPrecinctChooser(LinkedFieldMixin, AdminChooser):
    # icon = 'user'
    model = CountyJudicialPrecinct
    page_title = _("Choose a district")
    choose_modal_url_name = "county_judicial_precinct_chooser:choose"
    is_searchable = True
