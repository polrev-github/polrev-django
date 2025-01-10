from wagtail import hooks

from wagtail_modeladmin.options import ModelAdmin

from areas.models import StateJudicialDistrict

from areas.views import StateJudicialDistrictChooserViewSet

class StateJudicialDistrictAdmin(ModelAdmin):
    model = StateJudicialDistrict
    menu_label = 'State Judicial Districts'  # ditch this to use verbose_name_plural from model
    #menu_icon = 'pilcrow'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('title', 'district_num', 'state_ref')
    list_filter = ('state_ref',)
    search_fields = ('title',)

# Now you just need to register your customised ModelAdmin class with Wagtail
#modeladmin_register(StateJudicialDistrictAdmin)

@hooks.register('register_admin_viewset')
def register_state_judicial_district_chooser_viewset():
    return StateJudicialDistrictChooserViewSet('state_judicial_district_chooser', url_prefix='state-judicial-district-chooser')

