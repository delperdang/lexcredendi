from django.shortcuts import render
from prayer.models import Record

# Create your views here.
APP_NAME = 'prayer'
APP_FULL_NAME = 'Prayer Texts'
ICON_FILENAME = 'priest.svg'

def home(request):
    records = Record.objects.all().order_by('code')

    context = {
        'app_name': APP_NAME,
        'app_full_name': APP_FULL_NAME,
        'icon_filename': ICON_FILENAME,
        'records': records,
        'searchable': True
    }

    return render(request, 'home/home.html', context)

def details(request, code):
    record = Record.objects.get(pk=code)

    context = {
        'app_full_name': APP_FULL_NAME,
        'icon_filename': ICON_FILENAME,
        'record': record
    }

    return render(request, 'prayer/details.html', context)
