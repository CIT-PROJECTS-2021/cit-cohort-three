from keys import API_KEY
import requests
import json
import sys


class BaseURL:
    def __init__(self):
        self.base_url = 'https://api.apilayer.com/fixer/convert?to={}&from={}&amount={}'
        self.headers = {'apikey': API_KEY}
        self.symbols_url = 'https://api.apilayer.com/fixer/symbols'


class CurrencyConverter(BaseURL):
    def __init__(self):
        super().__init__()

    def convert(self, amount, from_currency, to_currency):
        url = self.base_url.format(to_currency, from_currency, amount)
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.text)['result']
        else:
            return 'Error: ' + response.text

    def get_symbols(self):
        response = requests.get(self.symbols_url, headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.text)['symbols']
        else:
            return 'Error: ' + response.text
