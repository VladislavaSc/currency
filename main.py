import json
import os
from datetime import datetime

import requests

API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')
CURRENCY_RATES_FILE = 'currency_rates.json'
def main():
    while True:
        currency = input('Enter currency name (USD or EUR): ')
        if currency not in ('USD', 'EUR'):
            print('Incorrect input')
            continue

        rate = get_currency_rate(currency)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print(f'Exchange rate {currency} to the ruble: {rate}')
        data = {'currency': currency, 'rate': rate, 'timestamp': timestamp}
        save_to_json(data)

        choice = input('Select an action (1 - continue, 2 - leave) ')
        if choice == '1':
            continue
        elif choice == '2':
            break
        else:
            print('Incorrect input')

def get_currency_rate(base: str) -> float:
    """Receives the exchange rate from the API and returns it as a float"""

    url = "https://api.apilayer.com/exchangerates_data/latest"
    response = requests.get(url, headers={'apikey': API_KEY}, params={'base': base})
    rate = response.json()['rates']['RUB']
    return rate

def save_to_json(data: dict) -> None:
    """Saves data to json file"""
    with open(CURRENCY_RATES_FILE, 'a') as f:
        if os.stat(CURRENCY_RATES_FILE).st_size == 0:
            json.dump([data], f)
        else:
            with open(CURRENCY_RATES_FILE) as f:
                data_list = json.load(f)
                data_list.append(data)
            with open(CURRENCY_RATES_FILE, 'w') as f:
                json.dump(data_list, f)


if __name__ == '__main__':
    print(get_currency_rate('USD'))
   # main()