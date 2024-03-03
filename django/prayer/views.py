from django.shortcuts import render
from django.db.models import Q
from prayer.models import Record

APP_NAME = 'prayer'
APP_FULL_NAME = 'Prayer Texts'
ICON_FILENAME = 'priest.svg'

def search(request):
    query = request.GET.get('q')
    records = Record.objects.filter(
        Q(code__icontains=query) | Q(title__icontains=query) | Q(text__icontains=query) | Q(latin_title__icontains=query) | Q(latin_text__icontains=query)
    )

    context = {
        'app_name': APP_NAME,
        'app_full_name': 'Filtered ' + APP_FULL_NAME,
        'icon_filename': ICON_FILENAME,
        'records': records,
        'searchable': True
    }

    return render(request, 'home/home.html', context)

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
