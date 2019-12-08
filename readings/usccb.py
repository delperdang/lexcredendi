'''
Captures the latest daily readings text and audio from the USCCB
'''

from datetime import datetime
import requests
import dateutil.parser as dparser
from bs4 import BeautifulSoup

# USCCB URL constants
USCCB_READINGS = 'http://www.usccb.org/bible/readings/{}.cfm'
USCCB_AUDIO = 'http://ccc.usccb.org/cccradio/NABPodcasts/nab_feed.xml'

def get_readings_url(local_now=datetime.now()):
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
        'RESPONSORIAL_TITLE': '',
        'RESPONSORIAL_TEXT': '',
        'READING_2_TITLE': '',
        'READING_2_TEXT': '',
        'ALLELUIA_TITLE': '',
        'ALLELUIA_TEXT': '',
        'GOSPEL_TITLE': '',
        'GOSPEL_TEXT': ''
    }
    headings = soup.find_all("h4")
    divs = soup.find_all("div", class_="poetry")
    for i in range(len(headings)):
        if 'READING 1' in headings[i].text.upper():
            print(headings[i].text)
            print(divs[i].text)
            readings['READING_1_TITLE'] = headings[i].text
            readings['READING_1_TEXT'] = divs[i].text.replace(',', ', ').replace('.', '. ').replace(';', '; ').replace(':', ': ').replace('?', '? ').replace('!', '! ').replace('  ', ' ').replace(', " ', '," ').replace('. " ', '." ').replace('; " ', ';" ').replace(': " ', ':" ').replace('? " ', '?" ').replace('! " ', '!" ')
        if 'RESPONSORIAL' in headings[i].text.upper():
            print(headings[i].text)
            print(divs[i].text)
            readings['RESPONSORIAL_TITLE'] = headings[i].text
            readings['RESPONSORIAL_TEXT'] = divs[i].text.replace(',', ', ').replace('.', '. ').replace(';', '; ').replace(':', ': ').replace('?', '? ').replace('!', '! ').replace('  ', ' ').replace(', " ', '," ').replace('. " ', '." ').replace('; " ', ';" ').replace(': " ', ':" ').replace('? " ', '?" ').replace('! " ', '!" ')
        if 'READING 2' in headings[i].text.upper():
            print(headings[i].text)
            print(divs[i].text)
            readings['READING_2_TITLE'] = headings[i].text
            readings['READING_2_TEXT'] = divs[i].text.replace(',', ', ').replace('.', '. ').replace(';', '; ').replace(':', ': ').replace('?', '? ').replace('!', '! ').replace('  ', ' ').replace(', " ', '," ').replace('. " ', '." ').replace('; " ', ';" ').replace(': " ', ':" ').replace('? " ', '?" ').replace('! " ', '!" ')
        if 'ALLELUIA' in headings[i].text.upper():
            print(headings[i].text)
            print(divs[i].text)
            readings['ALLELUIA_TITLE'] = headings[i].text
            readings['ALLELUIA_TEXT'] = divs[i].text.replace(',', ', ').replace('.', '. ').replace(';', '; ').replace(':', ': ').replace('?', '? ').replace('!', '! ').replace('  ', ' ').replace(', " ', '," ').replace('. " ', '." ').replace('; " ', ';" ').replace(': " ', ':" ').replace('? " ', '?" ').replace('! " ', '!" ')
        if 'GOSPEL' in headings[i].text.upper():
            print(headings[i].text)
            print(divs[i].text)
            readings['GOSPEL_TITLE'] = headings[i].text
            readings['GOSPEL_TEXT'] = divs[i].text.replace(',', ', ').replace('.', '. ').replace(';', '; ').replace(':', ': ').replace('?', '? ').replace('!', '! ').replace('  ', ' ').replace(', " ', '," ').replace('. " ', '." ').replace('; " ', ';" ').replace(': " ', ':" ').replace('? " ', '?" ').replace('! " ', '!" ')
    return readings

def extract_audio_url(soup, local_now=datetime.now()):
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

# execution code
readings_url = get_readings_url()
readings_soup = get_page_soup(readings_url)
audio_soup = get_page_soup(USCCB_AUDIO)
readings_context = assemble_readings_dict(readings_soup)
audio_url = extract_audio_url(audio_soup)
readings_context['AUDIO_URL'] = audio_url
