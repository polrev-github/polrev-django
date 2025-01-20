from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from .forms import UserCreationForm, LoginForm


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


class LogIn(LoginView):
    form_class = LoginForm
    # success_url = reverse_lazy('index')
    template_name = "accounts/login.html"


@login_required
def accounts(request):
    return render(request, "accounts/home.html")
