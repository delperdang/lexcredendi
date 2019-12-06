from django.shortcuts import render
from litcal.usccb import litcal_context

# Create your views here.

def home(request):
    return render(request, 'litcal/home.html', litcal_context)
