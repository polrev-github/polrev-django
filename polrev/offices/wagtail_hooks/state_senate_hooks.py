from wagtail import hooks

from wagtail_modeladmin.options import ModelAdmin
from offices.models import StateSenateOffice

from offices.views import StateSenateOfficeChooserViewSet


class StateSenateOfficeAdmin(ModelAdmin):
    model = StateSenateOffice
    menu_label = (
        "State Senate Offices"  # ditch this to use verbose_name_plural from model
    )
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
def register_state_senate_district_chooser_viewset():
    return StateSenateOfficeChooserViewSet(
        "state_senate_office_chooser", url_prefix="state-senate-office-chooser"
    )
