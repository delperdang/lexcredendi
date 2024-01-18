import requests
from bs4 import BeautifulSoup

class Catechism(object):
    '''
    Captures the url for every paragraph in the catechism
    '''
    # Vatican URL constants
    VATICAN_URL_PREFIX = 'https://www.vatican.va/archive/ENG0015/__P'
    VATICAN_URL_SUFFIX = '.HTM'

    def _convert_to_custom_system(self, num):
        """Converts an integer to a number in the system that counts 1-9 then A-Z before flipping the next digit."""

        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""

        while num > 0:
            remainder = num % 36  # Base 36 for 1-9 and A-Z
            result = digits[remainder] + result  # Append digit/letter to the beginning
            num //= 36  # Integer division for next digit

        return result

    def _get_page_soup(self, url, parser='html.parser'):
        '''
        retrieves web page soup for analysis
        '''
        response = requests.get(url)
        soup = BeautifulSoup(response.content, features=parser)
        return soup
    
    def _get_paragraphs(self):
        '''
        iterates through all pages of the catechism marking the location of each paragraph
        '''

        for paragraph in range(2865, 0, -1):
            for page in range(374, 0, -1):
                page_code = self._convert_to_custom_system(page)
                url = '{}{}{}'.format(self.VATICAN_URL_PREFIX,page_code,self.VATICAN_URL_SUFFIX)
