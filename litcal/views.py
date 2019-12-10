from django.shortcuts import render
from litcal.usccb import get_context

# Create your views here.

def home(request):
    context = get_context()
    return render(request, 'litcal/home.html', context)
