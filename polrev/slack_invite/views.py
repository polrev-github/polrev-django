# -*- coding: utf-8 -*-
import requests
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings

from .forms import InviteForm


def home(request):
    if request.method == "POST":
        form = InviteForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email_addr"]
            url = "https://" + settings.SLACK_URL + "/api/users.admin.invite"
            form = {"email": email, "token": settings.SLACK_TOKEN, "set_active": "true"}
            r = requests.post(url, data=form)
            print(r.text)
            return HttpResponseRedirect("/join-the-revolution-on-slack/thanks")
    else:
        form = InviteForm()
        community = settings.SLACK_TEAM
    return render(
        request, "slack_invite/index.html", {"form": form, "community": community}
    )


def thanks(request):
    community = settings.SLACK_TEAM
    return render(request, "slack_invite/thanks.html", {"community": community})
