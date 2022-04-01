from django.utils.translation import gettext_lazy as _

from generic_chooser.views import ModelChooserMixin, ModelChooserCreateTabMixin, ModelChooserViewSet

from areas.models import LocalCouncilDistrict
from areas.forms import LocalCouncilDistrictForm

class LocalCouncilDistrictChooserMixin(ModelChooserMixin):
    preserve_url_parameters = ['state_ref', 'place_ref',]  # preserve this URL parameter on pagination / search

    def get_unfiltered_object_list(self):
        objects = super().get_unfiltered_object_list()
        place_ref = self.request.GET.get('place_ref')
        if place_ref:
            objects = objects.filter(place_ref=place_ref)
        return objects

class LocalCouncilDistrictChooserCreateTabMixin(ModelChooserCreateTabMixin):
    def get_initial(self):
        data = self.initial.copy()
        state_ref = self.request.GET.get('state_ref')
        place_ref = self.request.GET.get('place_ref')
        data['state_ref'] = state_ref
        data['place_ref'] = place_ref
        return data

class LocalCouncilDistrictChooserViewSet(ModelChooserViewSet):
    chooser_mixin_class = LocalCouncilDistrictChooserMixin
    create_tab_mixin_class = LocalCouncilDistrictChooserCreateTabMixin
    form_class = LocalCouncilDistrictForm
    #icon = 'user'
    model = LocalCouncilDistrict
    page_title = _("Choose a district")
    per_page = 10
    #order_by = 'title'
    fields = ['state_ref', 'place_ref', 'title']

