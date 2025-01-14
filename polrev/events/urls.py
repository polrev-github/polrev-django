from django.urls import path
from . import views
from .views import event_heatmap

urlpatterns = [
    path('calendar/', views.calendar, name='calendar'),
    path('api/events/', views.api_events, name='api_events'),
    path('events/heatmap/', event_heatmap, name='event_heatmap'),
]