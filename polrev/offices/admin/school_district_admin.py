from django.contrib import admin
from offices.models import SchoolDistrictOffice


class SchoolDistrictOfficeAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ('state_ref',)

admin.site.register(SchoolDistrictOffice, SchoolDistrictOfficeAdmin)