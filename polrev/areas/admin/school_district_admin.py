from django.contrib import admin
from areas.models import SchoolDistrict

class SchoolDistrictAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ('state_ref',)

admin.site.register(SchoolDistrict, SchoolDistrictAdmin)