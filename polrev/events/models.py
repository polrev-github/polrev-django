from django.db import models
from django.shortcuts import render
from wagtail.models import Page
from .utils.heatmap import generate_heatmap


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    location = models.CharField(max_length=255)  # Store city, state, etc.
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class EventHeatmapPage(Page):
    template = 'events/heatmap.html'

    def serve(self, request):
        # Fetch event data and generate the heatmap
        events = Event.objects.all()
        heatmap_path = generate_heatmap(events)

        # Use Django's `render` to return the response
        return render(request, self.template, {'heatmap_path': heatmap_path})