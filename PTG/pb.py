import telebot
from datetime import datetime
from telebot import types

token = '5622855714:AAHvQH-zWE_gF-doRt2MRTvC5ntn-ysRRrs'
bot = telebot.TeleBot(token)
message_list_start = ['Привет', 'привет']

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

print(current_time)
print(type(current_time))

# curl "http://worldtimeapi.org/api/timezone/Europe/Moscow"
# цифры иконки https://vkclub.su/ru/emojis/sets/numbers/
# объявлем метод принятия текстового сообщения
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
# имя бота bot_unit18_j
# название бота Unit18_bot
# QAP95_GEREBIOV

# Done! Congratulations on your new bot. You will find it at t.me/Unit18_bot.
# You can now add a description, about section and profile picture for your bot, see /help for a list of commands.
# By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.
#
# Use this token to access the HTTP API:
# 5622855714:AAHvQH-zWE_gF-doRt2MRTvC5ntn-ysRRrs
# Keep your token secure and store it safely, it can be used by anyone to control your bot.
#
# For a description of the Bot API, see this page: https://core.telegram.org/bots/api
