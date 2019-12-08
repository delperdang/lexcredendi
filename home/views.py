import os
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'home/landing.html')

def mysuperuser(request):
    if not User.objects.filter(username='dieselpwr').exists():
        User.objects.create_superuser('dieselpwr', 'dieselpwr99@gmail.com', os.environ['SUPERUSER_PASS'])
    return render(request, 'home/landing.html')
