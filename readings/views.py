from django.shortcuts import render
from django.utils import timezone
import requests
import dateutil.parser as dparser
from dateutil import tz
from bs4 import BeautifulSoup

# Create your views here.


class USCCB(object):
    '''
    Captures the latest daily readings text and audio from the USCCB
    '''
    # USCCB URL constants
    USCCB_ROOT = 'http://www.usccb.org'
    USCCB_READINGS = 'http://www.usccb.org/bible/readings/{}.cfm'
    USCCB_AUDIO = 'http://ccc.usccb.org/cccradio/NABPodcasts/nab_feed.xml'

    def _get_readings_url(self, local_now):
        '''
        asembles readings url based on local time
        '''
        month_day_string = '{:%m%d}'.format(local_now)
        year_string = '{:%Y}'.format(local_now)[2:]
        date_string = '{}{}'.format(month_day_string, year_string)
        url = self.USCCB_READINGS.format(date_string)
        return url

    def _get_page_soup(self, url, parser='html.parser'):
        '''
        retrieves web page soup for analysis
        '''
        response = requests.get(url)
        soup = BeautifulSoup(response.content, features=parser)
        return soup

    def _assemble_readings_dict(self, soup):
        '''
        assembles readings dictionary from readings soup
        '''
        readings = {
            'READING_1_TITLE': '',
            'READING_1_TEXT': '',
            'READING_1_LINK': '',
            'READING_2_TITLE': '',
            'READING_2_TEXT': '',
            'READING_2_LINK': '',
            'GOSPEL_TITLE': '',
            'GOSPEL_TEXT': '',
            'GOSPEL_LINK': ''
        }
        headings = soup.find_all("h4")
        for heading in headings:
            if 'READING 1' in heading.text.upper():
                readings['READING_1_TITLE'] = 'Reading 1'
                readings['READING_1_TEXT'] = heading.a.text
                readings['READING_1_LINK'] = self.USCCB_ROOT + heading.a.get('href')
            if 'READING 2' in heading.text.upper():
                readings['READING_2_TITLE'] = 'Reading 2'
                readings['READING_2_TEXT'] = heading.a.text
                readings['READING_2_LINK'] = self.USCCB_ROOT + heading.a.get('href')
            if 'GOSPEL' in heading.text.upper():
                readings['GOSPEL_TITLE'] = 'Gospel'
                readings['GOSPEL_TEXT'] = heading.a.text
                readings['GOSPEL_LINK'] = self.USCCB_ROOT + heading.a.get('href')
        return readings

    def _extract_audio_url(self, soup, local_now):
        '''
        extracts audio url for current readings mp3
        '''
        url = ''
        local_now_date = local_now.date()
        items = soup.findAll('item')
        for item in items:
            pub_date = dparser.parse(item.pubdate.text, ignoretz=True).date()
            if local_now_date == pub_date:
                url = item.enclosure.get('url')
        return url

    def get_context(self, localtime):
        '''
        returns a context json of the current readings and audio
        '''
        readings_url = self._get_readings_url(localtime)
        readings_soup = self._get_page_soup(readings_url)
        audio_soup = self._get_page_soup(self.USCCB_AUDIO)
        readings_context = self._assemble_readings_dict(readings_soup)
        audio_url = self._extract_audio_url(audio_soup, localtime)
        readings_context['AUDIO_URL'] = audio_url
        return readings_context


def home(request):
    usccb = USCCB()
    context = usccb.get_context(timezone.localtime())
    return render(request, 'readings/home.html', context)
