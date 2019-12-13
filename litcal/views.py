from django.shortcuts import render
from django.utils import timezone
from litcal.usccb import get_context

# Create your views here.

def home(request):
    context = get_context(timezone.localtime())
    return render(request, 'litcal/home.html', context)
