from wagtail.contrib.modeladmin.options import ModelAdminGroup, modeladmin_register

from .office_hooks import *
from .state_hooks import *
from .us_senate_hooks import *
from .us_house_hooks import *
from .state_senate_hooks import *
from .state_house_hooks import *
from .county_hooks import *
from .local_hooks import *
from .local_council_hooks import *
from .county_council_hooks import *
from .school_district_hooks import *

class OfficeGroup(ModelAdminGroup):
    menu_label = 'Offices'
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (
        OfficeTypeAdmin,
        StateOfficeAdmin,
        UsSenateOfficeAdmin,
        UsHouseOfficeAdmin,
        StateSenateOfficeAdmin,
        StateHouseOfficeAdmin,
        CountyOfficeAdmin,
        LocalOfficeAdmin,
        LocalCouncilOfficeAdmin,
        CountyCouncilOfficeAdmin,
        SchoolDistrictOfficeAdmin
    )

modeladmin_register(OfficeGroup)
