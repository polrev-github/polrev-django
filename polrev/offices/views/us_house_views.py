from django.utils.translation import gettext_lazy as _

from generic_chooser.views import ModelChooserMixin, ModelChooserCreateTabMixin, ModelChooserViewSet

from offices.models import OfficeType, UsHouseOffice
from areas.models import CongressionalDistrict

class UsHouseOfficeChooserMixin(ModelChooserMixin):
    preserve_url_parameters = ['state_ref', 'district_ref',]  # preserve this URL parameter on pagination / search

    def get_unfiltered_object_list(self):
        objects = super().get_unfiltered_object_list()
        district_ref = self.request.GET.get('district_ref')
        if district_ref:
            objects = objects.filter(district_ref=district_ref)
        return objects

class UsHouseOfficeChooserCreateTabMixin(ModelChooserCreateTabMixin):
    def get_initial(self):
        data = self.initial.copy()
        state_ref = self.request.GET.get('state_ref')
        district_ref = self.request.GET.get('district_ref')

        district = CongressionalDistrict.objects.get(id=district_ref)
        data['type_ref'] = OfficeType.TYPE_US_HOUSE
        data['state_ref'] = state_ref
        data['district_ref'] = district_ref
        data['title'] = f"U.S. House, {district.title}"
        data['number'] = district.cd_num
        return data


class UsHouseOfficeChooserViewSet(ModelChooserViewSet):
    chooser_mixin_class = UsHouseOfficeChooserMixin
    create_tab_mixin_class = UsHouseOfficeChooserCreateTabMixin
    #icon = 'user'
    model = UsHouseOffice
    page_title = _("Choose an office")
    per_page = 10
    order_by = 'title'
    fields = ['type_ref', 'state_ref', 'district_ref', 'title', 'number', 'website']

