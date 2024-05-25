from django.shortcuts import render
from django.utils import timezone
from readings.readings import Readings

APP_NAME = 'readings'
APP_FULL_NAME = 'Daily Readings'
ICON_FILENAME = 'deacon.svg'

def home(request):
    readings = Readings()
    records = readings.get_records(timezone.localtime())

    context = {
        'app_full_name': APP_FULL_NAME,
        'icon_filename': ICON_FILENAME,
        'records': records
    }

    return render(request, 'home/scraped_home.html', context)
