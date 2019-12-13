'''
Captures the latest liturgical calendar entry from the usccb readings
'''

import requests
import dateutil.parser as dparser
from dateutil import tz
from bs4 import BeautifulSoup

# USCCB URL constants
USCCB_READINGS = 'http://www.usccb.org/bible/readings/{}.cfm'
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

def get_context(localtime):
    '''
    returns a context json of the current liturgical date
    '''
    readings_url = get_readings_url(localtime)
    readings_soup = get_page_soup(readings_url)
    litcal_context = assemble_litcal_dict(readings_soup)
    return litcal_context

