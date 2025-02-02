from django.contrib import admin
from areas.models import CongressionalDistrict


class CongressionalDistrictAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_filter = ("state_ref",)


admin.site.register(CongressionalDistrict, CongressionalDistrictAdmin)
