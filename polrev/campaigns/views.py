from django.shortcuts import render

def index(request):
    return render(request, 'campaigns/index.html')

def amascheduler(request):
    return render(request, 'campaigns/amascheduler.html')

