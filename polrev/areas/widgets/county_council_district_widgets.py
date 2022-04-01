from django.utils.translation import gettext_lazy as _

from generic_chooser.widgets import AdminChooser, LinkedFieldMixin

from areas.models import CountyCouncilDistrict

class CountyCouncilDistrictChooser(LinkedFieldMixin, AdminChooser):
    #icon = 'user'
    model = CountyCouncilDistrict
    page_title = _("Choose a district")
    choose_modal_url_name = 'county_council_district_chooser:choose'
    is_searchable = True