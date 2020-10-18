import requests
import re
import logging

from bs4 import BeautifulSoup

# The Pirate Bay (aka Tpb) handler class

class Tpb():

    def __init__(self):
        super().__init__()
        self.host = "https://tpb.party/"
        self.session = requests.Session()
        self.active_session = False
        self.logger = logging.getLogger(__name__)

    def build_search_url(self):
        return None

    def start_session(self):
        self.session.get(self.host)
        self.active_session = True

    def surf(self, name):
        if not self.active_session:
            self.start_session()

        results = self.session.get(
            self.host + 
            "search/" +
            name + "/"
            "1/99/0"
            )

        self.logger.debug(results.text)
        return results.text

    def _get_key_name(self, div):
        return div.a.string

    def _get_key_magnet(self, div):
        return div.find_next_sibling()['href']

    def _get_key_seeder(self, div):
        return int(div.find_next('td').string)

    def _get_key_size(self, div):
        size = div.find_next_sibling('font', class_='detDesc').contents
        # size = div.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().contents
        size_re = re.search("Size (.+)\,", size[0]).group(1)
        return size_re

    def get_results(self, name, count=10):   
        response_body = self.surf(name)
        soup = BeautifulSoup(response_body, 'html.parser')
        data = soup.find_all('div', class_='detName')
        results = []
        for dat in data:
            self.logger.debug(dat)
            results.append({
                    'name': self._get_key_name(dat),
                    'size': self._get_key_size(dat),
                    'seeder': self._get_key_seeder(dat),
                    'magnet': self._get_key_magnet(dat)
                })
        return results