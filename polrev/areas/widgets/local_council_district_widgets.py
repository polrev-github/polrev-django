from django.utils.translation import gettext_lazy as _

from generic_chooser.widgets import AdminChooser, LinkedFieldMixin

from areas.models import LocalCouncilDistrict

class LocalCouncilDistrictChooser(LinkedFieldMixin, AdminChooser):
    #icon = 'user'
    model = LocalCouncilDistrict
    page_title = _("Choose a district")
    choose_modal_url_name = 'local_council_district_chooser:choose'
    is_searchable = True