from wagtail.core import hooks

from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from offices.models import SchoolDistrictOffice
from offices.views import SchoolDistrictOfficeChooserViewSet

class SchoolDistrictOfficeAdmin(ModelAdmin):
    model = SchoolDistrictOffice
    menu_label = 'School District Offices'  # ditch this to use verbose_name_plural from model
    #menu_icon = 'pilcrow'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('title', 'lea_code', 'state_ref')
    list_filter = ('state_ref',)
    search_fields = ('title',)

# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(SchoolDistrictOfficeAdmin)

@hooks.register('register_admin_viewset')
def register_school_district_chooser_viewset():
    return SchoolDistrictOfficeChooserViewSet('school_district_office_chooser', url_prefix='school-district-office-chooser')

