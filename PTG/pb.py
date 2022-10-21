# имя бота bot_unit18_j
# название бота Unit18_bot
# QAP95_GEREBIOV

# Done! Congratulations on your new bot. You will find it at t.me/Unit18_bot.
# You can now add a description, about section and profile picture for your bot, see /help for a list of commands.
# By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for
# it. Just make sure the bot is fully operational before you do this.
#
# Use this token to access the HTTP API:
# 5622855714:AAHvQH-zWE_gF-doRt2MRTvC5ntn-ysRRrs
# Keep your token secure and store it safely, it can be used by anyone to control your bot.
# token = b'5622855714:AAHvQH-zWE_gF-doRt2MRTvC5ntn-ysRRrs'
# For a description of the Bot API, see this page: https://core.telegram.org/bots/api

import telebot
import os
import codecs
from datetime import datetime
from rsa import PrivateKey, decrypt

message_list_start = ['Привет', 'привет']
# time
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
folder = os.getcwd()

key_lust = [PrivateKey(
    8611358230186391020299884467627008805631867422184296025775040113155292187404091008391828212109012111160193892945618249623785973404528075573378180488699411,
    65537,
    1785289596312655367087515911037248709005907848470604850728679524809511495531410086323245025094710056967296658966006870838551894074625906357076875122535305,
    4976621894468449988039155076339535136070221736664167314792320432105946835123890807,
    1730362163892333445841066415765865910608387667078479960761628212597781573)]
prov_key = key_lust[0]
valid_bin = 'Unit18_bot.bin'


def token_key():
    if key_lust[0]:
        with open(os.path.join(folder, valid_bin), 'rb') as result:
            content = result.read()
            key_t_bot = decrypt(content, prov_key)
            result.close()
            res_token = codecs.decode(key_t_bot, 'UTF-8')
    return res_token


bot = telebot.TeleBot(token_key())


# curl "http://worldtimeapi.org/api/timezone/Europe/Moscow"
# цифры иконки https://vkclub.su/ru/emojis/sets/numbers/
# start метод принятия текстового сообщения


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, "🤖 Бот стартовал.")
    bot.send_message(message.from_user.id, "🤖 Введите /help чтобы узнать, что я умею.")


@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    if message.text in message_list_start:
        bot.send_message(message.from_user.id, "🤖 Привет! Чем я могу тебе помочь? /help")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, '🤖\n1⃣ Напиши привет\n2⃣ Точное время /time')
    elif message.text == "/time":
        bot.reply_to(message, "🤖 Время: " + str(datetime.now()))
    else:
        bot.send_message(message.from_user.id, "🤖 Для того чтобы узнать, что я умею напиши /help.")


bot.polling(none_stop=True, interval=0)
