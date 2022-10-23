import json
import telebot
from validbot import token_key
import requests

bot = token_key()
max_values = 3
keys = dict(биткоин='BTC', эфириум='ETH', доллар='USD')


class ConvertionException(Exception):
    pass


@bot.message_handler(commands=['start', 'help'])
def help_get(message: telebot.types.Message):
    text = "Для начала работы введите команды в следующем формате:\n<имя валюты>" \
           "<в какую валюту перевести>" \
           "<количество переводимой валюты>\n" \
           "/values - список доступной валюты"
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    values_input = message.text.split(' ')
    quote, base, amount = values_input


    if len(values_input) != 3:
        raise ConvertionException("Слишком много параметров.")

    quote_ticker, base_ticker = keys[quote], keys[base]
    if quote == base:
        raise ConvertionException(f"Вы ввели одинаковые значения валюты {base}")
    try:
        quote_ticker = keys[quote]
    except KeyError:
        raise ConvertionException(f"Не удалось обработать валюту {quote}")
    try:
        base_ticker = keys[base]
    except KeyError:
        raise ConvertionException(f"Не удалось обработать валюту {base}")
    try:
        amount = float(amount)
    except ValueError:
        raise ConvertionException(f"Не удалось обработать количество {amount}")

    r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")
    total_base = json.loads(r.content)[keys[base]]
    text = f"Стоимость {amount} {quote} в {base} составит {total_base} {base}."
    bot.send_message(message.chat.id, text)


bot.polling()

# bot.polling(none_stop=True, interval=0)
