from django.shortcuts import render
from piety.models import Record

# Create your views here.

def home(request):
    records = Record.objects.all().order_by('code')

    context = {
        'records': records
    }

    return render(request, 'piety/home.html', context)

def details(request, code):
    record = Record.objects.get(pk=code)

    context = {
        'record': record
    }

    return render(request, 'piety/details.html', context)
