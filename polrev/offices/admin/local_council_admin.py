from django.contrib import admin
from offices.models import LocalCouncilOffice

class LocalCouncilOfficeAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ('state_ref',)

admin.site.register(LocalCouncilOffice, LocalCouncilOfficeAdmin)