from django.contrib import admin
from offices.models import UsSenateOffice


class UsSenateOfficeAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_filter = ("state_ref",)


admin.site.register(UsSenateOffice, UsSenateOfficeAdmin)
