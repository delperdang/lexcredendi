from django.shortcuts import render
from art.models import Record

APP_NAME = 'art'
APP_FULL_NAME = 'Sacred Art'
ICON_FILENAME = 'eastern_cross.svg'

def get_unique_albums():
    '''
    returns unique albums and album_titles as code and title
    '''
    records = Record.objects.all().order_by('album')
    albums_json = []
    for record in records:
        temp_dict = {
            'code': "".join(char.upper() for char in record.album if char.isalpha()),
            'title': record.album
        }
        if temp_dict not in albums_json:
            albums_json.append(temp_dict)
    return albums_json

def home(request):
    records = get_unique_albums()

    context = {
        'app_name': APP_NAME,
        'app_full_name': APP_FULL_NAME,
        'icon_filename': ICON_FILENAME,
        'records': records
    }

    return render(request, 'home/home.html', context)

def details(request, album):
    records = Record.objects.filter(album=album).order_by('image')

    context = {
        'app_full_name': APP_FULL_NAME,
        'icon_filename': ICON_FILENAME,
        'records': records
    }

    return render(request, 'art/details.html', context)
