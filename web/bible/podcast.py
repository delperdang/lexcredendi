import requests
from bs4 import BeautifulSoup

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
