from django.shortcuts import render


def index(request):
    return render(request, "run/index.html")


def amascheduler(request):
    return render(request, "run/amascheduler.html")
