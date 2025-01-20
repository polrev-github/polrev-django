from wagtail import hooks

from wagtail_modeladmin.options import ModelAdmin
from offices.models import StateJudicialDistrictOffice
from offices.views import StateJudicialDistrictOfficeChooserViewSet


class StateJudicialDistrictOfficeAdmin(ModelAdmin):
    model = StateJudicialDistrictOffice
    menu_label = "State Judicial District Offices"  # ditch this to use verbose_name_plural from model
    # menu_icon = 'pilcrow'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = (
        False  # or True to exclude pages of this type from Wagtail's explorer view
    )
    list_display = ("title", "number", "state_ref")
    list_filter = ("state_ref",)
    search_fields = ("title",)


@hooks.register("register_admin_viewset")
def register_state_house_district_chooser_viewset():
    return StateJudicialDistrictOfficeChooserViewSet(
        "state_judicial_district_office_chooser",
        url_prefix="state-judicial-district-office-chooser",
    )
