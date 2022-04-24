from django.contrib import admin
from offices.models import StateSenateOffice

class StateSenateOfficeAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ('state_ref',)

admin.site.register(StateSenateOffice, StateSenateOfficeAdmin)
