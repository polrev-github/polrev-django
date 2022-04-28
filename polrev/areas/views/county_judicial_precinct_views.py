from django.utils.translation import gettext_lazy as _

from generic_chooser.views import ModelChooserMixin, ModelChooserCreateTabMixin, ModelChooserViewSet

from areas.models import CountyJudicialPrecinct

class CountyJudicialPrecinctChooserMixin(ModelChooserMixin):
    preserve_url_parameters = ['state_ref', 'county_ref',]  # preserve this URL parameter on pagination / search

    def get_unfiltered_object_list(self):
        objects = super().get_unfiltered_object_list()
        county_ref = self.request.GET.get('county_ref')
        if county_ref:
            objects = objects.filter(county_ref=county_ref)
        return objects

class CountyJudicialPrecinctChooserCreateTabMixin(ModelChooserCreateTabMixin):
    def get_initial(self):
        data = self.initial.copy()
        state_ref = self.request.GET.get('state_ref')
        county_ref = self.request.GET.get('county_ref')
        data['state_ref'] = state_ref
        data['county_ref'] = county_ref
        return data

class CountyJudicialPrecinctChooserViewSet(ModelChooserViewSet):
    chooser_mixin_class = CountyJudicialPrecinctChooserMixin
    create_tab_mixin_class = CountyJudicialPrecinctChooserCreateTabMixin
    #icon = 'user'
    model = CountyJudicialPrecinct
    page_title = _("Choose a district")
    per_page = 10
    #order_by = 'title'
    fields = ['state_ref', 'county_ref', 'name']

