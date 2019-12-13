'''
Captures the latest daily readings text and audio from the USCCB
'''

import requests
import dateutil.parser as dparser
from dateutil import tz
from bs4 import BeautifulSoup

# USCCB URL constants
USCCB_ROOT = 'http://www.usccb.org'
USCCB_READINGS = 'http://www.usccb.org/bible/readings/{}.cfm'
USCCB_AUDIO = 'http://ccc.usccb.org/cccradio/NABPodcasts/nab_feed.xml'
TARGET_TZ = 'America/New_York'

def get_readings_url(local_now):
    '''
    asembles readings url based on local time
    '''
    month_day_string = '{:%m%d}'.format(local_now)
    year_string = '{:%Y}'.format(local_now)[2:]
    date_string = '{}{}'.format(month_day_string, year_string)
    url = USCCB_READINGS.format(date_string)
    return url

def get_page_soup(url, parser='html.parser'):
    '''
    retrieves web page soup for analysis
    '''
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features=parser)
    return soup

def assemble_readings_dict(soup):
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
            readings['READING_1_LINK'] = USCCB_ROOT + heading.a.get('href')
        if 'READING 2' in heading.text.upper():
            readings['READING_2_TITLE'] = 'Reading 2'
            readings['READING_2_TEXT'] = heading.a.text
            readings['READING_2_LINK'] = USCCB_ROOT + heading.a.get('href')
        if 'GOSPEL' in heading.text.upper():
            readings['GOSPEL_TITLE'] = 'Gospel'
            readings['GOSPEL_TEXT'] = heading.a.text
            readings['GOSPEL_LINK'] = USCCB_ROOT + heading.a.get('href')
    return readings

def extract_audio_url(soup, local_now):
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

def get_context(localtime):
    '''
    returns a context json of the current readings and audio
    '''
    readings_url = get_readings_url(localtime)
    readings_soup = get_page_soup(readings_url)
    audio_soup = get_page_soup(USCCB_AUDIO)
    readings_context = assemble_readings_dict(readings_soup)
    audio_url = extract_audio_url(audio_soup, localtime)
    readings_context['AUDIO_URL'] = audio_url
    return readings_context
