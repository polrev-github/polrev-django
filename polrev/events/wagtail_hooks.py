from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from .models import Event

class EventAdmin(ModelAdmin):
    model = Event
    menu_label = "Events"
    menu_icon = "date"
    list_display = ("name", "date", "location")

modeladmin_register(EventAdmin)
