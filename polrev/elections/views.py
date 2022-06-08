from django.shortcuts import render

def index(request):
    return render(request, 'elections/index.html')

def amascheduler(request):
    return render(request, 'elections/amascheduler.html')

