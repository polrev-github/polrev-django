from django.utils.translation import gettext_lazy as _

from generic_chooser.views import ModelChooserMixin, ModelChooserCreateTabMixin, ModelChooserViewSet

from offices.models import OfficeType, StateSenateOffice
from areas.models import StateSenateDistrict

class StateSenateOfficeChooserMixin(ModelChooserMixin):
    preserve_url_parameters = ['district_ref',]  # preserve this URL parameter on pagination / search

    def get_unfiltered_object_list(self):
        objects = super().get_unfiltered_object_list()
        district_ref = self.request.GET.get('district_ref')
        if district_ref:
            objects = objects.filter(district_ref=district_ref)
        return objects


class StateSenateOfficeChooserCreateTabMixin(ModelChooserCreateTabMixin):
    def get_initial(self):
        data = self.initial.copy()
        state_ref = self.request.GET.get('state_ref')
        district_ref = self.request.GET.get('district_ref')
        print('XXXXXXXXXXX')
        print(district_ref)
        district = StateSenateDistrict.objects.get(id=district_ref)
        data['type_ref'] = OfficeType.TYPE_STATE_SENATE
        data['state_ref'] = state_ref
        data['district_ref'] = district_ref
        data['title'] = f"State Senate, {district.title}"
        return data


class StateSenateOfficeChooserViewSet(ModelChooserViewSet):
    chooser_mixin_class = StateSenateOfficeChooserMixin
    create_tab_mixin_class = StateSenateOfficeChooserCreateTabMixin
    icon = 'user'
    model = StateSenateOffice
    page_title = _("Choose a district")
    per_page = 10
    #order_by = 'title'
    fields = ['type_ref', 'state_ref', 'district_ref', 'title', 'website']
