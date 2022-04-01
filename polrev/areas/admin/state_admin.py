from django.contrib import admin
from areas.models import State

class StateAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ('state_usps',)

admin.site.register(State, StateAdmin)