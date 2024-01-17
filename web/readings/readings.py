import requests
import dateutil.parser as dparser
from dateutil.parser._parser import ParserError
from bs4 import BeautifulSoup

class Readings(object):
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
        print(url)
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
        readings = []
        headings = soup.find_all('div', {'class': 'content-header'})
        for heading in headings:
            if 'READING 1' in heading.text.upper() or 'READING I' in heading.text.upper():
                if heading.a.get('href', '').startswith('http'):
                    temp_link = heading.a.get('href')
                elif heading.a.get('href', '').startswith('/'):
                    temp_link = self.USCCB_ROOT + heading.a.get('href')
                else:
                    temp_link = self.USCCB_ROOT + '/' + heading.a.get('href')
                temp_citation = heading.a.text
                temp_title = 'Reading 1'
                temp_text = '<a href="{}">{}</a>'.format(temp_link, temp_citation)
                readings.append(
                    {
                        'title': temp_title,
                        'text': temp_text,
                    }
                )
            if 'READING 2' in heading.text.upper() or 'READING II' in heading.text.upper():
                if heading.a.get('href', '').startswith('http'):
                    temp_link = heading.a.get('href')
                elif heading.a.get('href', '').startswith('/'):
                    temp_link = self.USCCB_ROOT + heading.a.get('href')
                else:
                    temp_link = self.USCCB_ROOT + '/' + heading.a.get('href')
                temp_citation = heading.a.text
                temp_title = 'Reading 2'
                temp_text = '<a href="{}">{}</a>'.format(temp_link, temp_citation)
                readings.append(
                    {
                        'title': temp_title,
                        'text': temp_text,
                    }
                )
            if 'RESPONSORIAL PSALM' in heading.text.upper():
                if heading.a.get('href', '').startswith('http'):
                    temp_link = heading.a.get('href')
                elif heading.a.get('href', '').startswith('/'):
                    temp_link = self.USCCB_ROOT + heading.a.get('href')
                else:
                    temp_link = self.USCCB_ROOT + '/' + heading.a.get('href')
                temp_citation = heading.a.text
                temp_title = 'Responsorial Psalm'
                temp_text = '<a href="{}">{}</a>'.format(temp_link, temp_citation)
                readings.append(
                    {
                        'title': temp_title,
                        'text': temp_text,
                    }
                )
            if 'GOSPEL' in heading.text.upper():
                if heading.a.get('href', '').startswith('http'):
                    temp_link = heading.a.get('href')
                elif heading.a.get('href', '').startswith('/'):
                    temp_link = self.USCCB_ROOT + heading.a.get('href')
                else:
                    temp_link = self.USCCB_ROOT + '/' + heading.a.get('href')
                temp_citation = heading.a.text
                temp_title = 'Gospel'
                temp_text = '<a href="{}">{}</a>'.format(temp_link, temp_citation)
                readings.append(
                    {
                        'title': temp_title,
                        'text': temp_text,
                    }
                )
        return readings

    def _extract_audio(self, soup, local_now):
        '''
        extracts audio url for current readings mp3
        '''
        url = ''
        local_now_date = local_now.date()
        items = soup.findAll('item')
        for item in items:
            title_text = item.title.text
            title_text_date_left = title_text.split('For ')[-1].split(',')[0]
            title_text_date_right = title_text.split(',')[-1][0:5]
            title_text_date = "{},{}".format(title_text_date_left,title_text_date_right) 
            try:
                title_date = dparser.parse(title_text_date, ignoretz=True).date()
                if local_now_date == title_date:
                    url = item.enclosure.get('url')
            except ParserError as err:
                # TODO: figure out a better way to parse dates from RSS feed
                print(err)
        audio = {
            'title': 'Complete Audio',
            'text': '<a href="{}">{}</a>'.format(url, 'Click to play')
        }
        return audio

    def get_records(self, localtime):
        '''
        returns a context json of the current readings and audio
        '''
        readings_url = self._get_readings_url(localtime)
        readings_soup = self._get_page_soup(readings_url)
        audio_soup = self._get_page_soup(self.USCCB_AUDIO)
        readings_records = self._assemble_readings_dict(readings_soup)
        audio_record = self._extract_audio(audio_soup, localtime)
        readings_records.append(audio_record)
        return readings_records
