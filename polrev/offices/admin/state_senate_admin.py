from django.contrib import admin
from areas.models import StateSenateDistrict, StateHouseDistrict

class StateSenateDistrictAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ('state_ref',)

admin.site.register(StateSenateDistrict, StateSenateDistrictAdmin)

class StateHouseDistrictAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ('state_ref',)

admin.site.register(StateHouseDistrict, StateHouseDistrictAdmin)