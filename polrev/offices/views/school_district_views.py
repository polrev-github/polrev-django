from django.utils.translation import gettext_lazy as _

from generic_chooser.views import ModelChooserMixin, ModelChooserCreateTabMixin, ModelChooserViewSet

from offices.models import OfficeType, SchoolDistrictOffice
from areas.models import SchoolDistrict


class SchoolDistrictOfficeChooserMixin(ModelChooserMixin):
    preserve_url_parameters = ['state_ref', 'district_ref', 'office_type_ref']

    def get_unfiltered_object_list(self):
        objects = super().get_unfiltered_object_list()
        district_ref = self.request.GET.get('district_ref')
        if district_ref:
            objects = objects.filter(district_ref=district_ref)
        return objects


class SchoolDistrictOfficeChooserCreateTabMixin(ModelChooserCreateTabMixin):
    def get_initial(self):
        data = self.initial.copy()
        state_ref = self.request.GET.get('state_ref')
        district_ref = self.request.GET.get('district_ref')
        type_ref = self.request.GET.get('office_type_ref')
        print('XXXXXXXXXXX')
        print(district_ref)
        district = SchoolDistrict.objects.get(id=district_ref)
        data['state_ref'] = state_ref
        data['district_ref'] = district_ref
        data['type_ref'] = type_ref
        office_type = OfficeType.objects.get(id=type_ref)
        data['title'] = f"{office_type.title}, {district.title}"
        data['number'] = int(district.lea_code)
        return data

class SchoolDistrictOfficeChooserViewSet(ModelChooserViewSet):
    chooser_mixin_class = SchoolDistrictOfficeChooserMixin
    create_tab_mixin_class = SchoolDistrictOfficeChooserCreateTabMixin
    icon = 'user'
    model = SchoolDistrictOffice
    page_title = _("Choose an office")
    per_page = 10
    #order_by = 'title'
    fields = ['type_ref', 'state_ref', 'district_ref', 'title', 'number', 'website']

