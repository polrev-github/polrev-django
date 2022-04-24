from django.contrib import admin
from offices.models import LocalOffice

class LocalOfficeAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ('state_ref',)

admin.site.register(LocalOffice, LocalOfficeAdmin)