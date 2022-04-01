from django.utils.translation import gettext_lazy as _

from generic_chooser.views import ModelChooserMixin, ModelChooserCreateTabMixin, ModelChooserViewSet

from offices.models import OfficeType, CountyOffice
from areas.models import County

class CountyOfficeChooserMixin(ModelChooserMixin):
    preserve_url_parameters = ['state_ref', 'county_ref', 'office_type_ref']

    def get_unfiltered_object_list(self):
        objects = super().get_unfiltered_object_list()
        county_ref = self.request.GET.get('county_ref')
        if county_ref:
            objects = objects.filter(county_ref=county_ref)
        return objects


class CountyOfficeChooserCreateTabMixin(ModelChooserCreateTabMixin):
    def get_initial(self):
        data = self.initial.copy()
        state_ref = self.request.GET.get('state_ref')
        county_ref = self.request.GET.get('county_ref')
        type_ref = self.request.GET.get('office_type_ref')
        print('XXXXXXXXXXX')
        print(county_ref)
        county = County.objects.get(id=county_ref)
        data['state_ref'] = state_ref
        data['county_ref'] = county_ref
        data['type_ref'] = type_ref
        office_type = OfficeType.objects.get(id=type_ref)
        data['title'] = f"{office_type.title}, {county.title}"
        return data

class CountyOfficeChooserViewSet(ModelChooserViewSet):
    chooser_mixin_class = CountyOfficeChooserMixin
    create_tab_mixin_class = CountyOfficeChooserCreateTabMixin
    icon = 'user'
    model = CountyOffice
    page_title = _("Choose an office")
    per_page = 10
    #order_by = 'title'
    fields = ['type_ref', 'state_ref', 'county_ref', 'title', 'website']

