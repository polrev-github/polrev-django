from wagtail.core import hooks

from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from areas.models import CongressionalDistrict

from areas.views import CongressionalDistrictChooserViewSet

class CongressionalDistrictAdmin(ModelAdmin):
    model = CongressionalDistrict
    menu_label = 'Congressional Districts'  # ditch this to use verbose_name_plural from model
    #menu_icon = 'pilcrow'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('title', 'cd_fips', 'state_ref')
    list_filter = ('state_ref',)
    search_fields = ('title',)

# Now you just need to register your customised ModelAdmin class with Wagtail
#modeladmin_register(CongressionalDistrictAdmin)

@hooks.register('register_admin_viewset')
def register_congressional_district_chooser_viewset():
    return CongressionalDistrictChooserViewSet('congressional_district_chooser', url_prefix='congressional-district-chooser')

