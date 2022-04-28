from django.utils.translation import gettext_lazy as _

from generic_chooser.views import ModelChooserMixin, ModelChooserViewSet

from areas.models import StateJudicialDistrict

class StateJudicialDistrictChooserMixin(ModelChooserMixin):
    preserve_url_parameters = ['state_ref',]  # preserve this URL parameter on pagination / search

    def get_unfiltered_object_list(self):
        objects = super().get_unfiltered_object_list()
        state_ref = self.request.GET.get('state_ref')
        if state_ref:
            objects = objects.filter(state_ref=state_ref)
        return objects


class StateJudicialDistrictChooserViewSet(ModelChooserViewSet):
    chooser_mixin_class = StateJudicialDistrictChooserMixin
    #icon = 'user'
    model = StateJudicialDistrict
    page_title = _("Choose a district")
    per_page = 10
    #order_by = 'title'
    fields = ['title']

