from wagtail import hooks

from wagtail_modeladmin.options import ModelAdmin

from offices.models import UsHouseOffice

from offices.views import UsHouseOfficeChooserViewSet


class UsHouseOfficeAdmin(ModelAdmin):
    model = UsHouseOffice
    menu_label = (
        "U.S. House Offices"  # ditch this to use verbose_name_plural from model
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
def register_congressional_district_chooser_viewset():
    return UsHouseOfficeChooserViewSet(
        "us_house_office_chooser", url_prefix="us-house-office-chooser"
    )
