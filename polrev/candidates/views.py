from django.shortcuts import render

def home(request):
    return render(request, 'candidates/home.html')

def amascheduler(request):
    return render(request, 'candidates/amascheduler.html')

