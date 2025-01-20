from django.contrib import admin
from offices.models import StateOffice


class StateOfficeAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_filter = ("state_ref",)


admin.site.register(StateOffice, StateOfficeAdmin)
