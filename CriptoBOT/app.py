import json
import telebot
from validbot import token_key
import requests



bot = token_key()

keys = {
    'биткоин': 'BTC',
    'эфириум': 'ETH',
    'доллар': 'USD',
}


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
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



@bot.message_handler(chat_types=['text'])
def convert(message: telebot.types.Message):
    quote, base, amount = message.text.split(' ')
    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
    text = json.loads(r.content)[keys[base]]
    bot.send_message(message.chat.id, text)



# bot.polling()

bot.polling(none_stop=True, interval=0)
