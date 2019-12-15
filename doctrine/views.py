from django.shortcuts import render
from doctrine.models import Record

# Create your views here.
APP_NAME = 'doctrine'
APP_FULL_NAME = 'Doctrinal Formulae'
ICON_FILENAME = 'pope.svg'

def home(request):
    records = Record.objects.all().order_by('code')

    context = {
        'app_name': APP_NAME,
        'app_full_name': APP_FULL_NAME,
        'icon_filename': ICON_FILENAME,
        'records': records
    }

    return render(request, 'home/home.html', context)

def details(request, code):
    record = Record.objects.get(pk=code)

    context = {
        'app_full_name': APP_FULL_NAME,
        'icon_filename': ICON_FILENAME,
        'record': record
    }

    return render(request, 'home/details.html', context)
