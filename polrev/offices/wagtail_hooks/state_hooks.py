from wagtail.core import hooks

from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from offices.models import StateOffice
from offices.views import StateOfficeChooserViewSet

class StateOfficeAdmin(ModelAdmin):
    model = StateOffice
    menu_label = 'State Offices'  # ditch this to use verbose_name_plural from model
    #menu_icon = 'pilcrow'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('title', 'state_ref')
    list_filter = ('state_ref',)
    search_fields = ('title',)

# Now you just need to register your customised ModelAdmin class with Wagtail
#modeladmin_register(StateOfficeAdmin)

@hooks.register('register_admin_viewset')
def register_state_office_chooser_viewset():
    return StateOfficeChooserViewSet('state_office_chooser', url_prefix='state-office-chooser')

