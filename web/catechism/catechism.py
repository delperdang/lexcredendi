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
    
    def get_paragraphs_xref(self):
        '''
        iterates through all pages of the catechism marking the location of each paragraph
        '''
        paragraph_url_xref = {}
        for paragraph_num in range(2865, 0, -1):
            paragraph_found = False
            for page_num in range(374, 0, -1):
                page_code = self._convert_to_custom_system(page_num)
                url = '{}{}{}'.format(self.VATICAN_URL_PREFIX,page_code,self.VATICAN_URL_SUFFIX)
                soup = self._get_page_soup(url)
                paragraphs = soup.find_all('p', {'class': 'MsoNormal'})
                for paragraph in paragraphs:
                    if paragraph.text.startswith(str(paragraph_num)):
                        paragraph_url_xref[str(paragraph_num)] = url
                        paragraph_found = True
                        break
                if paragraph_found:
                    break
        return paragraph_url_xref

catechism = Catechism()
paragraph_url_xref = catechism.get_paragraphs_xref()                
import json
with open("paragraph_url_xref.json", "w") as f:
    json.dump(paragraph_url_xref, f, indent=4)