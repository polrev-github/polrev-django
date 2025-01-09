#from wagtail_modeladmin.options import ModelAdminGroup, modeladmin_register
from wagtail_modeladmin.options import ModelAdminGroup, modeladmin_register

from .state_hooks import *
from .congressional_district_hooks import *
from .legislative_district_hooks import *
from .county_hooks import *
from .place_hooks import *
from .local_council_district_hooks import *
from .county_council_district_hooks import *
from .school_district_hooks import *

from .state_judicial_district_hooks import *

class AreaGroup(ModelAdminGroup):
    menu_label = 'Areas'
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (
        StateAdmin,
        CongressionalDistrictAdmin,
        StateSenateDistrictAdmin,
        StateHouseDistrictAdmin,
        CountyAdmin,
        PlaceAdmin,
        LocalCouncilDistrictAdmin,
        CountyCouncilDistrictAdmin,
        SchoolDistrictAdmin,

        StateJudicialDistrictAdmin,
    )

modeladmin_register(AreaGroup)
