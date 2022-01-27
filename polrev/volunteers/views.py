from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from accounts.models import User

def index(request):
    return render(request, 'volunteers/index.html')
