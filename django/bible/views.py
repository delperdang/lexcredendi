from django.shortcuts import render
from django.db.models import Q
from django.utils import timezone
from bible.models import Record
from home.podcast import Podcast
from home.bible import Bible

APP_NAME = 'bible'
APP_FULL_NAME = 'Bible in a Year'
ICON_FILENAME = 'bible.svg'

def search(request):
    query = request.GET.get('q')
    records = Record.objects.filter(
        Q(code__icontains=query) | Q(title__icontains=query) | Q(text__icontains=query)
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
    
    day_code = 'DAY' + timezone.localtime().date().strftime('%j')
    print(day_code)
    for record in records:
        if record.code == day_code:
            record.highlight = True

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
    
    podcast = Podcast('bibleinayear')
    record = podcast.update_record(record)

    bible = Bible()
    record.text = bible.linkify(record.text)

    context = {
        'app_full_name': APP_FULL_NAME,
        'icon_filename': ICON_FILENAME,
        'record': record
    }

    return render(request, 'home/details.html', context)
