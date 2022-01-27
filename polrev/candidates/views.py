from django.shortcuts import render

def index(request):
    return render(request, 'candidates/index.html')

def amascheduler(request):
    return render(request, 'candidates/amascheduler.html')

