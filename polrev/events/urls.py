from django.urls import path
from . import views

urlpatterns = [
    path('calendar/', views.calendar, name='calendar'),
    path('api/events/', views.api_events, name='api_events'),
]