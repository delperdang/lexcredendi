from django.shortcuts import render


APP_NAME = 'meditation'
APP_FULL_NAME = 'Breathing Meditation'
ICON_FILENAME = 'crucifix.svg'

def home(request):

    context = {
        'app_full_name': APP_FULL_NAME,
        'icon_filename': ICON_FILENAME
    }

    return render(request, 'meditation/home.html', context)
