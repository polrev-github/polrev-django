from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='campaign'),
    path('amascheduler/', views.amascheduler, name='amascheduler'),
]
