import os
import codecs
import telebot
from rsa import PrivateKey, decrypt

# RSA
key_lust = [PrivateKey(
    8611358230186391020299884467627008805631867422184296025775040113155292187404091008391828212109012111160193892945618249623785973404528075573378180488699411,
    65537,
    1785289596312655367087515911037248709005907848470604850728679524809511495531410086323245025094710056967296658966006870838551894074625906357076875122535305,
    4976621894468449988039155076339535136070221736664167314792320432105946835123890807,
    1730362163892333445841066415765865910608387667078479960761628212597781573)]
prov_key = key_lust[0]
valid_bin = 'Unit18_bot.bin'
folder = os.getcwd()


# Чтение токена из бинарного файла, предоставление переменной с ним
def token_key():
    if key_lust[0]:
        with open(os.path.join(folder, valid_bin), 'rb') as result:
            content = result.read()
            key_t_bot = decrypt(content, prov_key)
            result.close()
            res_token = codecs.decode(key_t_bot, 'UTF-8')
            bot_res = telebot.TeleBot(res_token)
    return bot_res
