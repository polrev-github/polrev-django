from django.contrib import admin
from offices.models import UsHouseOffice

class UsHouseOfficeAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ('state_ref',)

admin.site.register(UsHouseOffice, UsHouseOfficeAdmin)