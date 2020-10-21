import random
import requests
import logging
import urllib.parse, base64, time

class Snowfl():

    def __init__(self):
        super().__init__()
        self.host = "https://snowfl.com/"
        self.token = "OIcObqNfqpHTDvLKWQDNRlzQPbtqRcoKhtlled"
        self.rng_token_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP1234567890"
        self.rng_token_length = 8
        self.session = requests.Session()
        self.active_session = False
        self.logger = logging.getLogger(__name__)
    
    def get_rng_token(self):
        return ''.join(random.sample(self.rng_token_set, self.rng_token_length))

    def build_search_url(self):
        return None

    def start_session(self):
        self.session.get(self.host)
        self.active_session = True

    def _request_magnet_1337x(self, url):
        url_encoded = urllib.parse.quote_plus(url)
        url_encoded_byte = url_encoded.encode('ascii')
        url_base64_byte = base64.b64encode(url_encoded_byte)
        url_base64 = url_base64_byte.decode('ascii')

        results = self.session.get(
            self.host + 
            self.token + "/1337x/" + 
            url_base64 +
            "?_=1602628388020"
            )
        
        time.sleep(1)
        
        if results.status_code == 503:
            return None
        else:
            return results.json()['url']

    # Request URL: https://snowfl.com/OIcObqNfqpHTDvLKWQDNRlzQPbtqRcoKhtlled/1337x/aHR0cHMlM0ElMkYlMkYxMzM3eC50byUyRnRvcnJlbnQlMkYzNzc1NDU5JTJGQmlnTmF0dXJhbHMtMTktMDUtMjItTGEtU2lyZW5hLU1hc3NhZ2UtV2l0aC1Ucmlja3MlMkY=?_=1602703136192


    def _get_key(self, key, dict_data):
        if key in dict_data:
            return dict_data[key]
        else:
            if key=='magnet' and dict_data['site']=='1337x':
                return self._request_magnet_1337x(dict_data['url'])
            else:
                return None

    def surf(self, name):

        if not self.active_session:
            self.start_session()

        results = self.session.get(
            self.host + 
            self.token + "/" + 
            name + "/" +
            self.get_rng_token() + "/" +
            "0/NONE/NONE/1?_=1602628388020"
            )

        # self.logger.debug(f"{results.json()}")
        return results.json()

    def get_results(self, name, count=10):
        data = self.surf(name)
        results = []
        for dat in data:
            results.append({
                'name': self._get_key('name', dat),
                'magnet': self._get_key('magnet', dat),
                'seeder': self._get_key('seeder', dat),
                'size': self._get_key('size', dat),
                'age': self._get_key('age', dat)
            })
        return results