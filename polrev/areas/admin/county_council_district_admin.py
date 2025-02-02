from django.contrib import admin
from areas.models import CountyCouncilDistrict


class CountyCouncilDistrictAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_filter = ("state_ref",)


admin.site.register(CountyCouncilDistrict, CountyCouncilDistrictAdmin)
