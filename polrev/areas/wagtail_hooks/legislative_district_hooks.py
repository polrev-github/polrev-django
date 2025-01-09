from wagtail import hooks

from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from areas.models import StateSenateDistrict, StateHouseDistrict

from areas.views import StateSenateDistrictChooserViewSet, StateHouseDistrictChooserViewSet

class StateSenateDistrictAdmin(ModelAdmin):
    model = StateSenateDistrict
    menu_label = 'State Senate Districts'  # ditch this to use verbose_name_plural from model
    #menu_icon = 'pilcrow'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('title', 'district_num', 'seats', 'state_ref')
    list_filter = ('state_ref',)
    search_fields = ('title',)

# Now you just need to register your customised ModelAdmin class with Wagtail
#modeladmin_register(StateSenateDistrictAdmin)

class StateHouseDistrictAdmin(ModelAdmin):
    model = StateHouseDistrict
    menu_label = 'State House Districts'  # ditch this to use verbose_name_plural from model
    #menu_icon = 'pilcrow'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('title', 'district_num', 'seats', 'state_ref')
    list_filter = ('state_ref',)
    search_fields = ('title',)

# Now you just need to register your customised ModelAdmin class with Wagtail
#modeladmin_register(StateHouseDistrictAdmin)

@hooks.register('register_admin_viewset')
def register_state_senate_district_chooser_viewset():
    return StateSenateDistrictChooserViewSet('state_senate_district_chooser', url_prefix='state-senate-district-chooser')

@hooks.register('register_admin_viewset')
def register_state_house_district_chooser_viewset():
    return StateHouseDistrictChooserViewSet('state_house_district_chooser', url_prefix='state-house-district-chooser')

