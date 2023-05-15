from datetime import datetime
import requests
import json

import os

API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')
def main():
    while True:
        currency = input('Enter currency name (USD or EUR): ')
        if currency not in ('USD', 'EUR'):
            print('Incorrect input')
            continue

        rate = get_currency_rate(currency)
        timestamp = datetime.now()

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
    pass

def save_to_json(data):
    pass

if __name__ == '__main__':
    main()