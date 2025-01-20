from django.urls import path

from .views import home, thanks

urlpatterns = [
    path("", home, name="home"),
    path("thanks/", thanks, name="thanks"),
]
