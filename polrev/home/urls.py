from django.urls import path
from . import views

urlpatterns = [
    path("phonebanking/", views.phonebanking, name="phonebanking"),
    path("about-us/", views.about, name="about"),
    path("issues/", views.issues, name="issues"),
    path("transparency/", views.transparency, name="transparency"),
    #path("privacy-policy/", views.privacy, name="privacy"),
]
