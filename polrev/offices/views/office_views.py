from django.utils.translation import gettext_lazy as _

from generic_chooser.views import ModelChooserMixin, ModelChooserViewSet

from offices.models import OfficeType
from offices.forms import OfficeTypeForm


class OfficeTypeChooserMixin(ModelChooserMixin):
    def get_unfiltered_object_list(self):
        objects = super().get_unfiltered_object_list()
        objects = objects.all()
        return objects


class OfficeTypeChooserViewSet(ModelChooserViewSet):
    chooser_mixin_class = OfficeTypeChooserMixin
    form_class = OfficeTypeForm
    icon = "user"
    model = OfficeType
    page_title = _("Choose an office type")
    per_page = 10
    fields = ["title"]
