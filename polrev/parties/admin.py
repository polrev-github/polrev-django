from django.contrib import admin
from .models import Party

class PartyAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(Party, PartyAdmin)