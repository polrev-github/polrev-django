from django.urls import path
from . import views

urlpatterns = [
    path("", views.accounts, name="accounts"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("login/", views.LogIn.as_view(), name="login"),
]
