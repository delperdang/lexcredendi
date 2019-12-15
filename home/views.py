import os
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils import timezone
import requests

# Create your views here.

def fetch_updates():
    '''
    retrieves last 10 commits from github
    '''
    updates_json = []
    commits_json = requests.get('https://api.github.com/repos/dieselpwr/lexcredendi/commits').json()[:5]
    for commit in commits_json:
        updates_json.append(
            {
                'author': commit['commit']['author']['name'],
                'date': commit['commit']['author']['date'],
                'message': commit['commit']['message']

            }
        )
    return updates_json

def home(request):
    updates = fetch_updates()

    context = {
        'updates': updates
    }

    return render(request, 'home/landing.html', context)

def mysuperuser(request):
    if not User.objects.filter(username=os.environ['SUPERUSER_NAME']).exists():
        User.objects.create_superuser(os.environ['SUPERUSER_NAME'], os.environ['SUPERUSER_EMAL'], os.environ['SUPERUSER_PASS'])
        html = 'created'
    else:
        html = 'exists'
    return HttpResponse(html)

def localtime(request):
    now = timezone.localtime()
    html = str(now)
    return HttpResponse(html)