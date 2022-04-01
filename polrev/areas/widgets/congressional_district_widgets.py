from django.utils.translation import gettext_lazy as _

from generic_chooser.widgets import AdminChooser, LinkedFieldMixin

from areas.models import CongressionalDistrict

class CongressionalDistrictChooser(LinkedFieldMixin, AdminChooser):
    #icon = 'user'
    model = CongressionalDistrict
    page_title = _("Choose a district")
    choose_modal_url_name = 'congressional_district_chooser:choose'