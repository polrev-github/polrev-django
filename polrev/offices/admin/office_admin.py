from django.contrib import admin
from offices.models import OfficeType, Office

class OfficeTypeAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(OfficeType, OfficeTypeAdmin)

'''
class OfficeAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(Office, OfficeAdmin)
'''