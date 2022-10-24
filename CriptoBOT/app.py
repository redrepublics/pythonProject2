import telebot
from Exept_pars import ConvertionException, CryptoConverter
from app_params import bot, keys, max_values, robot_sm, message_list_start
from telebot import types


# обработка команд, интерфейсные кнопки
@bot.message_handler(commands=['start', 'help'])
def help_get(message: telebot.types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    pad1 = types.KeyboardButton(text='/help')
    pad2 = types.KeyboardButton(text='/values')
    keyboard.add(pad1, pad2)

    if message.text in message_list_start[1]:
        bot.send_message(message.from_user.id,
                         f"{robot_sm} Здравствуйте {message.chat.username}.\n "
                         f"Для того чтобы узнать, что я умею, воспользуйтесь кнопками.",
                         reply_markup=keyboard)
    elif message.text in message_list_start[0]:
        bot.send_message(message.from_user.id,
                         f"{robot_sm} Для начала работы введите команды в следующем формате:\n <конвертируемая "
                         f"валюта><валюта конвертации><сумма>\n "
                         f"{robot_sm} Пример: рубль доллар 10", reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id,
                         f"{robot_sm} Доброго времени суток, {message.chat.username}! Введите /help чтобы "
                         f"узнать, что я умею.", reply_markup=keyboard)


# Обработка и вывод параметров
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = f'{robot_sm} Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


# обработка текстового ввода и контроль ко-ва параметров
@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values_input = message.text.split(' ')
        if len(values_input) != max_values:
            if len(values_input) > max_values:
                raise ConvertionException(f"{robot_sm} Слишком много параметров. Введите 3 параметр.")
            elif len(values_input) < max_values:
                raise ConvertionException(f"{robot_sm} Слишком мало параметров. Введите 3 параметр.")
        else:
            pass
        quote, base, amount = values_input
        total_base = CryptoConverter.convert_s(quote, base, amount)
    except ConvertionException as per_f:
        bot.reply_to(message, f"{robot_sm} Ошибка ввода.\n{per_f}")
    except Exception as per_f:
        bot.reply_to(message, f"{robot_sm} Что-то сломалось. Мы уже чиним это! {per_f}")
    else:
        text = f"{robot_sm} Конвертация {quote} в {base}:\n{amount} {quote} после конвертации будет {total_base} {base}"
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True, interval=0)
