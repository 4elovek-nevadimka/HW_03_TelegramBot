import json
import requests
from config import keys


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise APIException(f'Конвертация одинаковых валют {base} не имеет смысла! Результат равен {amount}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Неверно указано название валюты {quote}!')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Неверно указано название валюты {base}!')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Неверно указано количество {amount}!')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        return float(json.loads(r.content)[keys[base]])
