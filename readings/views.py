from django.shortcuts import render
from readings.usccb import get_context

# Create your views here.

def home(request):
    context = get_context()
    return render(request, 'readings/home.html', context)
