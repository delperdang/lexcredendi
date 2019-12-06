from django.shortcuts import render
from readings.usccb import readings_context

# Create your views here.

def home(request):
    return render(request, 'readings/home.html', readings_context)
