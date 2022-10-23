import telebot
from Exept_pars import ConvertionException, CryptoConverter
from app_params import bot, keys, max_values
from telebot import types


@bot.message_handler(commands=['start', 'help'])
def help_get(message: telebot.types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    pad1 = types.KeyboardButton(text='/start')
    pad2 = types.KeyboardButton(text='/help')
    pad3 = types.KeyboardButton(text='/values')
    keyboard.add(pad1, pad2, pad3)
    text = "Для начала работы введите команды в следующем формате:\n<имя валюты>" \
           "<в какую валюту перевести>" \
           "<количество переводимой валюты>"
    bot.reply_to(message, text, reply_markup=keyboard)




@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)



@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values_input = message.text.split(' ')
        if len(values_input) != max_values:
            if len(values_input) > max_values:
                raise ConvertionException("Слишком много параметров. Введите 3 параметр.")
            elif len(values_input) < max_values:
                raise ConvertionException("Слишком мало параметров. Введите 3 параметр.")
        else:
            pass
        quote, base, amount = values_input
        total_base = CryptoConverter.convert_s(quote, base, amount)
    except ConvertionException as per_f:
        bot.reply_to(message, f"Ошибка ввода.\n{per_f}")
    except Exception as per_f:
        bot.reply_to(message, f"Что-то сломалось. Мы уже чиним это! {per_f}")
    else:
        text = f"Конвертация {quote} в {base}:\n{amount} {quote} после конвертации будет  {total_base} {base}"
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True, interval=0)
