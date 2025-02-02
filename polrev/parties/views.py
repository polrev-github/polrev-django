from django.utils.translation import gettext_lazy as _

from generic_chooser.views import ModelChooserMixin, ModelChooserViewSet

from parties.models import Party

#TODO: This isn't being used anywhere?

class PartyChooserMixin(ModelChooserMixin):
    preserve_url_parameters = ["state_ref", "office_type_ref"]

    def get_unfiltered_object_list(self):
        objects = super().get_unfiltered_object_list()
        state_ref = self.request.GET.get("state_ref")
        if state_ref:
            objects = objects.filter(state_ref=state_ref)
        return objects


class PartyChooserViewSet(ModelChooserViewSet):
    chooser_mixin_class = PartyChooserMixin
    icon = "user"
    model = Party
    page_title = _("Choose a Party")
    per_page = 10
    fields = ["type_ref", "state_ref", "title", "website"]
