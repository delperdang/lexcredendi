from datetime import date
from django.shortcuts import render
from django.utils import timezone
import requests
import dateutil.parser as dparser
from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd
from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU
from dateutil import tz
from bs4 import BeautifulSoup

# Create your views here.
APP_NAME = 'litcal'
APP_FULL_NAME = 'Liturgical Calendar'
ICON_FILENAME = 'cathedral.svg'


class USCCBCalendar(object):
    '''
    Captures the latest liturgical calendar entry from the usccb readings
    '''

    # USCCB URL constants
    USCCB_READINGS = 'http://www.usccb.org/bible/readings/{}.cfm'

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

    def _assemble_litcal_dict(self, soup):
        '''
        assembles readings dictionary from readings soup
        '''
        litcal = {
            'title': '',
            'text': ''
        }
        headings = soup.find_all("h3")
        for heading in headings:
            if 'Lectionary' in heading.text:

                litcal['title'] = soup.title.string
                litcal['text'] = heading.text.split('Lectionary')[0]
        return litcal

    def get_record(self, localtime):
        '''
        returns a context json of the current liturgical date
        '''
        readings_url = self._get_readings_url(localtime)
        readings_soup = self._get_page_soup(readings_url)
        litcal_record = self._assemble_litcal_dict(readings_soup)
        return litcal_record


class USCCBIntentions(object):
    '''
    captures the latest list of intentions from the holy Father by month from the usccb
    '''

    # USCCB URL constants
    USCCB_INTENTIONS = 'http://www.usccb.org/prayer-and-worship/prayers-and-devotions/the-popes-monthly-intention.cfm'

    def _get_month(self, local_now):
        '''
        returns the current day of week spelled out and uppercased
        '''
        month = local_now.date().strftime("%B").upper()
        return month

    def _get_page_soup(self, url, parser='html.parser'):
        '''
        retrieves web page soup for analysis
        '''
        response = requests.get(url)
        soup = BeautifulSoup(response.content, features=parser)
        return soup

    def _assemble_intentions_dict(self, soup, month):
        '''
        assembles readings dictionary from readings soup
        '''
        intention = {
            'title': "This Month's Papal Intentions",
            'text': ''
        }
        next_p = soup.find(text=month).parent.find_next_sibling("p")
        intention['text'] = next_p.text.replace("\n", ": ")
        return intention

    def get_record(self, localtime):
        '''
        returns a context json of the current liturgical date
        '''
        month_string = self._get_month(localtime)
        intentions_soup = self._get_page_soup(self.USCCB_INTENTIONS)
        intentions_record = self._assemble_intentions_dict(soup=intentions_soup, month=month_string)
        return intentions_record


class Mysteries(object):
    '''
    Determines the appropriate mysteries of the Rosary for the given day and season
    '''

    # Rosary Mysteries constants
    JOYFUL_MYSTERIES = {'title': "Today's Mysteries of the Rosary", 'text': '<a href="/doctrine/details/JOYFUL_MYSTERIES">Joyful Mysteries</a>'}
    SORROWFUL_MYSTERIES = {'title': "Today's Mysteries of the Rosary", 'text': '<a href="/doctrine/details/SORROWFUL_MYSTERIES">Sorrowful Mysteries</a>'}
    GLORIOUS_MYSTERIES = {'title': "Today's Mysteries of the Rosary", 'text': '<a href="/doctrine/details/GLORIOUS_MYSTERIES">Glorious Mysteries</a>'}
    LUMINOUS_MYSTERIES = {'title': "Today's Mysteries of the Rosary", 'text': '<a href="/doctrine/details/LUMINOUS_MYSTERIES">Luminous Mysteries</a>'}

    def _get_season(self, local_now):
        '''
        returns the current liturgical season using local time
        '''
        baptism_of_our_lord = date(local_now.year, 1, 6) + rd(days=1, weekday=SU(+1))
        ash_wednesday = easter(local_now.year) - rd(days=46)
        maundy_thursday = easter(local_now.year) - rd(days=3)
        pentecost = easter(local_now.year) + rd(days=49)
        first_sunday_of_advent = date(local_now.year, 12, 25) - rd(days=1, weekday=SU(-4))
        christmas = date(local_now.year, 12, 25)
        season = 'ORDINARY'
        if local_now.date() < baptism_of_our_lord:
            season = 'CHRISTMAS'
        elif local_now.date() >= baptism_of_our_lord and local_now.date() < ash_wednesday:
            season = 'ORDINARY'
        elif local_now.date() >= ash_wednesday and local_now.date() < maundy_thursday:
            season = 'LENT'
        elif local_now.date() >= maundy_thursday and local_now.date() < easter(local_now.year):
            season = 'TRIDUUM'
        elif local_now.date() >= easter(local_now.year) and local_now.date() < pentecost:
            season = 'EASTER'
        elif local_now.date() >= pentecost and local_now.date() < first_sunday_of_advent:
            season = 'ORDINARY'
        elif local_now.date() >= first_sunday_of_advent and local_now.date() < christmas:
            season = 'ADVENT'
        elif local_now.date() >= christmas:
            season = 'CHRISTMAS'
        return season

    def _get_upper_day_of_week(self, local_now):
        '''
        returns the current day of week spelled out and uppercased
        '''
        day_of_week = local_now.date().strftime("%A").upper()
        return day_of_week

    def get_record(self, localtime):
        '''
        returns a context json of the current liturgical date
        '''
        season_string = self._get_season(localtime)
        dow_string = self._get_upper_day_of_week(localtime)
        rosary_record = {}
        if dow_string == 'SUNDAY' and season_string == 'ADVENT':
            rosary_record = self.JOYFUL_MYSTERIES
        elif dow_string == 'SUNDAY' and season_string == 'LENT':
            rosary_record = self.SORROWFUL_MYSTERIES
        elif dow_string == 'SUNDAY' and season_string == 'TRIDUUM':
            rosary_record = self.SORROWFUL_MYSTERIES
        elif dow_string == 'SUNDAY':
            rosary_record = self.GLORIOUS_MYSTERIES
        elif dow_string == 'MONDAY':
            rosary_record = self.JOYFUL_MYSTERIES
        elif dow_string == 'TUESDAY':
            rosary_record = self.SORROWFUL_MYSTERIES
        elif dow_string == 'WEDNESDAY':
            rosary_record = self.GLORIOUS_MYSTERIES
        elif dow_string == 'THURSDAY':
            rosary_record = self.LUMINOUS_MYSTERIES
        elif dow_string == 'FRIDAY':
            rosary_record = self.SORROWFUL_MYSTERIES
        elif dow_string == 'SATURDAY':
            rosary_record = self.JOYFUL_MYSTERIES
        return rosary_record


def home(request):
    records = []
    usccb_calendar = USCCBCalendar()
    usccb_calendar_record = usccb_calendar.get_record(timezone.localtime())
    records.append(usccb_calendar_record)
    mysteries = Mysteries()
    mysteries_record = mysteries.get_record(timezone.localtime())
    records.append(mysteries_record)
    usccb_intentions = USCCBIntentions()
    usccb_intentions_record = usccb_intentions.get_record(timezone.localtime())
    records.append(usccb_intentions_record)

    context = {
        'app_full_name': APP_FULL_NAME,
        'icon_filename': ICON_FILENAME,
        'records': records
    }

    return render(request, 'litcal/home.html', context)
