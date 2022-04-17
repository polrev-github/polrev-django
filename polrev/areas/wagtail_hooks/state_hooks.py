from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from areas.models import State


class StateAdmin(ModelAdmin):
    model = State
    menu_label = 'States'  # ditch this to use verbose_name_plural from model
    #menu_icon = 'pilcrow'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('title', 'state_fips', 'state_usps')
    list_filter = ('state_usps',)
    search_fields = ('title', 'state_usps')

# Now you just need to register your customised ModelAdmin class with Wagtail
#modeladmin_register(StateAdmin)