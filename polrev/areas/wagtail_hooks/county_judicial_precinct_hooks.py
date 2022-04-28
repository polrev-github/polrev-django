from wagtail.core import hooks

from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from areas.models import CountyJudicialPrecinct

from areas.views import CountyJudicialPrecinctChooserViewSet

class CountyJudicialPrecinctAdmin(ModelAdmin):
    model = CountyJudicialPrecinct
    menu_label = 'County Judicial Precincts'  # ditch this to use verbose_name_plural from model
    #menu_icon = 'pilcrow'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('title', 'state_ref', 'county_ref')
    list_filter = ('state_ref',)
    search_fields = ('title',)

# Now you just need to register your customised ModelAdmin class with Wagtail
#modeladmin_register(CountyJudicialPrecinctAdmin)

@hooks.register('register_admin_viewset')
def register_county_council_district_chooser_viewset():
    return CountyJudicialPrecinctChooserViewSet('county_judicial_precint_chooser', url_prefix='county-judicial-precinct-chooser')

