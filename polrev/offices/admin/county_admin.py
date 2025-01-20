from django.contrib import admin
from offices.models import CountyOffice


class CountyOfficeAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_filter = ("state_ref",)


admin.site.register(CountyOffice, CountyOfficeAdmin)
