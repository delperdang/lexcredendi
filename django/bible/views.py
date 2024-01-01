from django.shortcuts import render
from django.db.models import Q
from bible.models import Record
import requests
from bs4 import BeautifulSoup


APP_NAME = 'bible'
APP_FULL_NAME = 'Bible in a Year'
ICON_FILENAME = 'bible.svg'

class Podcast(object):
    '''
    Captures the associated podcast data for a target record
    '''
    # Podcast URL constants
    RSS_FEED = 'https://feeds.fireside.fm/bibleinayear/rss'

    def _get_page_soup(self, url, parser='html.parser'):
        '''
        retrieves web page soup for analysis
        '''
        response = requests.get(url)
        soup = BeautifulSoup(response.content, features=parser)
        return soup

    def _extract_audio(self, soup, record):
        '''
        extracts audio url for target date mp3
        '''
        url = ''
        day_code = record.code
        items = soup.findAll('item')
        for item in items:
            title_text = item.title.text
            title_day_code = title_text.upper().replace(" ","").split(':')[0]
            if day_code == title_day_code:
                url = item.enclosure.get('url')
        audio_link = '<br><a href="{}">{}</a>'.format(url, 'Click to play')
        return audio_link

    def update_record(self, record):
        '''
        returns an updated record object with podcast data
        '''
        audio_soup = self._get_page_soup(self.RSS_FEED)
        audio_link = self._extract_audio(audio_soup, record)
        record.text += audio_link
        return record


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
    
    podcast = Podcast()
    record = podcast.update_record(record)

    context = {
        'app_full_name': APP_FULL_NAME,
        'icon_filename': ICON_FILENAME,
        'record': record
    }

    return render(request, 'home/details.html', context)
