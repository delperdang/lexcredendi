'''
Captures the latest liturgical calendar entry from the usccb readings
'''

from datetime import datetime
import requests
import dateutil.parser as dparser
from dateutil import tz
from bs4 import BeautifulSoup

# USCCB URL constants
USCCB_READINGS = 'http://www.usccb.org/bible/readings/{}.cfm'
TARGET_TZ = 'America/New_York'

def get_now():
    '''
    builds the current now in local time
    '''
    utc_now = datetime.now()
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz(TARGET_TZ)
    utc_now.replace(tzinfo=from_zone)
    target_now = utc_now.astimezone(to_zone)
    return target_now

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

def get_context():
    '''
    returns a context json of the current liturgical date
    '''
    now = get_now()
    readings_url = get_readings_url(now)
    readings_soup = get_page_soup(readings_url)
    litcal_context = assemble_litcal_dict(readings_soup)
    return litcal_context

