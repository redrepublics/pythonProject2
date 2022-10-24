import json
import requests
from app_params import keys, robot_sm


# Базовый класс обработки ошибок
class ConvertionException(Exception):
    pass


# Наследственный класс обработки ошибок в работе с основными параметрами. Возврат правильного параметра.
class CryptoConverter:
    @staticmethod
    def convert_s(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f"{robot_sm} Вы ввели одинаковые значения валюты {base}")
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f"{robot_sm} Не удалось обработать валюту {quote}")
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f"{robot_sm} Не удалось обработать валюту {base}")
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f"{robot_sm}Не удалось обработать количество {amount}")
        quote_ticker, base_ticker = keys[quote], keys[base]
        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")
        total_base = json.loads(r.content)[keys[base]] * amount
        return total_base
