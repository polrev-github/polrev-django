from django.contrib import admin
from areas.models import Place


class PlaceAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_filter = ("state_ref",)
    filter_horizontal = ("counties",)


admin.site.register(Place, PlaceAdmin)
