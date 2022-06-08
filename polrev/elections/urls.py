from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='election'),
    path('amascheduler/', views.amascheduler, name='amascheduler'),
]
