from django.contrib import admin
from offices.models import StateJudicialDistrictOffice


class StateJudicialDistrictOfficeAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_filter = ("state_ref",)


admin.site.register(StateJudicialDistrictOffice, StateJudicialDistrictOfficeAdmin)
