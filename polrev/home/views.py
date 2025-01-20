from django.shortcuts import render


def phonebanking(request):
    return render(request, "home/phonebanking.html")


def about(request):
    return render(request, "home/about.html")


def mission(request):
    return render(request, "home/mission.html")


def by_laws(request):
    return render(request, "home/by_laws.html")


def issues(request):
    return render(request, "home/issues.html")


def transparency(request):
    return render(request, "home/transparency.html")


def privacy(request):
    return render(request, "home/privacy.html")
