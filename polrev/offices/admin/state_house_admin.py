from django.contrib import admin
from offices.models import StateHouseOffice


class StateHouseOfficeAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_filter = ("state_ref",)


admin.site.register(StateHouseOffice, StateHouseOfficeAdmin)
