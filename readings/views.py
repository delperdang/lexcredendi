from django.shortcuts import render
from django.utils import timezone
from readings.usccb import get_context

# Create your views here.

def home(request):
    context = get_context(timezone.localtime())
    return render(request, 'readings/home.html', context)
