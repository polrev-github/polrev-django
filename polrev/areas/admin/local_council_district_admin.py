from django.contrib import admin
from areas.models import LocalCouncilDistrict


class LocalCouncilDistrictAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_filter = ("state_ref",)


admin.site.register(LocalCouncilDistrict, LocalCouncilDistrictAdmin)
