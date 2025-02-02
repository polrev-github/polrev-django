from django.contrib import admin
from areas.models import County


class CountyAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_filter = ("state_ref",)


admin.site.register(County, CountyAdmin)
