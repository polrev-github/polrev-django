from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='candidate'),
    path('amascheduler/', views.amascheduler, name='amascheduler'),
]