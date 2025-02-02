from django.contrib import admin
from areas.models import StateJudicialDistrict


class StateJudicialDistrictAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_filter = ("state_ref",)


admin.site.register(StateJudicialDistrict, StateJudicialDistrictAdmin)
