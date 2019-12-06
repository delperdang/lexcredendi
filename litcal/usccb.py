'''
Captures the latest daily readings text and audio from the USCCB
'''

from datetime import datetime
import requests
import dateutil.parser as dparser
from bs4 import BeautifulSoup

# USCCB URL constants
USCCB_READINGS = 'http://www.usccb.org/bible/readings/{}.cfm'

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

def assemble_litcal_dict(soup):
    '''
    assembles readings dictionary from readings soup
    '''
    litcal = {
        'CALENDAR_DAY': '',
        'LITURGICAL_DAY': '',
    }
    headings = soup.find_all("h3")
    for heading in headings:
        if 'Lectionary' in heading.text:
            litcal['CALENDAR_DAY'] = soup.title.string
            litcal['LITURGICAL_DAY'] = heading.text.split('Lectionary')[0]
    return litcal

# execution code
readings_url = get_readings_url()
readings_soup = get_page_soup(readings_url)
litcal_context = assemble_litcal_dict(readings_soup)
