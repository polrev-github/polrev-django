from wagtail import hooks

from wagtail_modeladmin.options import ModelAdmin, modeladmin_register

from offices.models import CountyCouncilOffice
from offices.views import CountyCouncilOfficeChooserViewSet

class CountyCouncilOfficeAdmin(ModelAdmin):
    model = CountyCouncilOffice
    menu_label = 'County Council Offices'  # ditch this to use verbose_name_plural from model
    #menu_icon = 'pilcrow'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('title', 'state_ref', 'county_ref', 'district_ref')
    list_filter = ('state_ref',)
    search_fields = ('title',)
    autocomplete_fields = ['county_ref']

# Now you just need to register your customised ModelAdmin class with Wagtail
#modeladmin_register(CountyCouncilOfficeAdmin)

@hooks.register('register_admin_viewset')
def register_county_chooser_viewset():
    return CountyCouncilOfficeChooserViewSet('county_council_office_chooser', url_prefix='county-council-office-chooser')

