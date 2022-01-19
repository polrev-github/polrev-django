from django.urls import path

from .views import home, amascheduler

urlpatterns = [
    path('', home, name='home'),
    path('amascheduler/', amascheduler, name='amascheduler'),
]
