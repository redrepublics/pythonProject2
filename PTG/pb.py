import telebot
from datetime import datetime


bot = telebot.TeleBot('5622855714:AAHvQH-zWE_gF-doRt2MRTvC5ntn-ysRRrs')
message_list_start = ['Привет', 'привет']

now = datetime.now()
current_time = now.strftime("%H:%M:%S")







# объявлем метод принятия текстового сообщения
@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    if message.text in message_list_start:
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, 'Напиши привет \n' 'Узнать точное время /time')
    elif message.text == "/time":
        with current_time as f:
            bot.send_message(message.from_user.id, 'Точное время:', f)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)
# имя бота bot_unit18_j
# название бота Unit18_bot

# Done! Congratulations on your new bot. You will find it at t.me/Unit18_bot.
# You can now add a description, about section and profile picture for your bot, see /help for a list of commands.
# By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.
#
# Use this token to access the HTTP API:
# 5622855714:AAHvQH-zWE_gF-doRt2MRTvC5ntn-ysRRrs
# Keep your token secure and store it safely, it can be used by anyone to control your bot.
#
# For a description of the Bot API, see this page: https://core.telegram.org/bots/api
