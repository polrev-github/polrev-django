from django.utils.translation import gettext_lazy as _

from generic_chooser.views import ModelChooserMixin, ModelChooserCreateTabMixin, ModelChooserViewSet

from offices.models import OfficeType, LocalCouncilOffice
from offices.forms import LocalCouncilOfficeForm
from areas.models import Place

class LocalCouncilOfficeChooserMixin(ModelChooserMixin):
    preserve_url_parameters = ['state_ref', 'place_ref', 'district_ref', 'office_type_ref']

    def get_unfiltered_object_list(self):
        objects = super().get_unfiltered_object_list()
        place_ref = self.request.GET.get('place_ref')
        if place_ref:
            objects = objects.filter(place_ref=place_ref)
        return objects


class LocalCouncilOfficeChooserCreateTabMixin(ModelChooserCreateTabMixin):
    def get_initial(self):
        data = self.initial.copy()
        state_ref = self.request.GET.get('state_ref')
        place_ref = self.request.GET.get('place_ref')
        district_ref = self.request.GET.get('district_ref')
        type_ref = self.request.GET.get('office_type_ref')
        print('XXXXXXXXXXX')
        print(place_ref)
        place = Place.objects.get(id=place_ref)
        data['state_ref'] = state_ref
        data['place_ref'] = place_ref
        data['district_ref'] = district_ref
        data['type_ref'] = type_ref
        office_type = OfficeType.objects.get(id=type_ref)
        data['title'] = f"{office_type.title}, {place.title}"
        return data

class LocalCouncilOfficeChooserViewSet(ModelChooserViewSet):
    chooser_mixin_class = LocalCouncilOfficeChooserMixin
    create_tab_mixin_class = LocalCouncilOfficeChooserCreateTabMixin
    form_class = LocalCouncilOfficeForm
    icon = 'user'
    model = LocalCouncilOffice
    page_title = _("Choose an office")
    per_page = 10
    #order_by = 'title'
    fields = ['type_ref', 'state_ref', 'place_ref', 'district_ref', 'title', 'website']

