from django.utils.translation import gettext_lazy as _

from generic_chooser.views import ModelChooserMixin, ModelChooserCreateTabMixin, ModelChooserViewSet

from parties.models import Party

class PartyChooserMixin(ModelChooserMixin):
    preserve_url_parameters = ['state_ref', 'office_type_ref']

    def get_unfiltered_object_list(self):
        objects = super().get_unfiltered_object_list()
        state_ref = self.request.GET.get('state_ref')
        if state_ref:
            objects = objects.filter(state_ref=state_ref)
        return objects

'''
class PartyChooserCreateTabMixin(ModelChooserCreateTabMixin):
    def get_initial(self):
        data = self.initial.copy()
        state_ref = self.request.GET.get('state_ref')
        type_ref = self.request.GET.get('office_type_ref')
        print('XXXXXXXXXXX')
        print(state_ref)
        state = State.objects.get(id=state_ref)
        data['state_ref'] = state_ref
        data['type_ref'] = type_ref
        office_type = OfficeType.objects.get(id=type_ref)
        data['title'] = f"{office_type.title}, {state.title}"
        return data
'''

class PartyChooserViewSet(ModelChooserViewSet):
    chooser_mixin_class = PartyChooserMixin
    #create_tab_mixin_class = PartyChooserCreateTabMixin
    icon = 'user'
    model = Party
    page_title = _("Choose a Party")
    per_page = 10
    #order_by = 'title'
    fields = ['type_ref', 'state_ref', 'title', 'website']

