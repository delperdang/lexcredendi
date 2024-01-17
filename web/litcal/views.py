from django.shortcuts import render
from django.utils import timezone
from litcal.calendar import Calendar
from litcal.intentions import Intentions
from litcal.mysteries import Mysteries

APP_NAME = 'litcal'
APP_FULL_NAME = 'Liturgical Calendar'
ICON_FILENAME = 'cathedral.svg'

def home(request):
    records = []
    usccb_calendar = Calendar()
    usccb_calendar_record = usccb_calendar.get_record(timezone.localtime())
    records.append(usccb_calendar_record)
    mysteries = Mysteries()
    mysteries_record = mysteries.get_record(timezone.localtime())
    records.append(mysteries_record)
    usccb_intentions = Intentions()
    usccb_intentions_record = usccb_intentions.get_record(timezone.localtime())
    records.append(usccb_intentions_record)

    context = {
        'app_full_name': APP_FULL_NAME,
        'icon_filename': ICON_FILENAME,
        'records': records
    }

    return render(request, 'home/scraped_home.html', context)
