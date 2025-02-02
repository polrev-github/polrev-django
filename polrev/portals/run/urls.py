from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="run"),
    path("amascheduler/", views.amascheduler, name="amascheduler"),
]
