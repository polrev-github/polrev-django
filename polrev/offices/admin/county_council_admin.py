from django.contrib import admin
from offices.models import CountyCouncilOffice


class CountyCouncilOfficeAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_filter = ("state_ref",)


admin.site.register(CountyCouncilOffice, CountyCouncilOfficeAdmin)
