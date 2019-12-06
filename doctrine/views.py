from django.shortcuts import render
from doctrine.models import Record

# Create your views here.

def home(request):
    records = Record.objects.all().order_by('code')

    context = {
        'records': records
    }

    return render(request, 'doctrine/home.html', context)

def details(request, code):
    record = Record.objects.get(pk=code)

    context = {
        'record': record
    }

    return render(request, 'doctrine/details.html', context)
