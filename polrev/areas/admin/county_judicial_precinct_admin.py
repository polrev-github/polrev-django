from django.contrib import admin
from areas.models import CountyJudicialPrecinct

class CountyJudicialPrecinctAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ('state_ref',)

admin.site.register(CountyJudicialPrecinct, CountyJudicialPrecinctAdmin)