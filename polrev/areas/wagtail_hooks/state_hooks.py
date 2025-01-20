from wagtail_modeladmin.options import ModelAdmin
from areas.models import State


class StateAdmin(ModelAdmin):
    model = State
    menu_label = "States"
    # menu_icon = 'pilcrow'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = (
        False  # or True to exclude pages of this type from Wagtail's explorer view
    )
    list_display = ("title", "state_fips", "state_usps")
    list_filter = ("state_usps",)
    search_fields = ("title", "state_usps")
