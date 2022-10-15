import rsa, os
from GetParser import dir_cr, folder_dir, folder_dir_return
folder = os.getcwd()
# RSA - криптографический алгоритм с открытым ключем. При создании приложения вы
# генерируете два ключа: публичный (открытый) и приватный (закрытый).
# Открытый ключ передается всем желающим и заинтерисованным.
# С его помошью можно зашифровать данные.
# А вот расшифровать можно только знаю другой ключ из пары (т.е. закрытый),
# его мы никому не скажем даже под страхом смерти
# (pubkey, privkey) = rsa.newkeys(512) - сгенерить новые ключи по необходимости

KeyParserAspo = b'17110367'
key_lust = []
key_lust.append(rsa.PublicKey(8611358230186391020299884467627008805631867422184296025775040113155292187404091008391828212109012111160193892945618249623785973404528075573378180488699411, 65537))
key_lust.append(rsa.PrivateKey(8611358230186391020299884467627008805631867422184296025775040113155292187404091008391828212109012111160193892945618249623785973404528075573378180488699411, 65537, 1785289596312655367087515911037248709005907848470604850728679524809511495531410086323245025094710056967296658966006870838551894074625906357076875122535305, 4976621894468449988039155076339535136070221736664167314792320432105946835123890807, 1730362163892333445841066415765865910608387667078479960761628212597781573))
pubkey = key_lust[0]
privkey = key_lust[1]
if KeyParserAspo:
    crypto = rsa.encrypt(KeyParserAspo, pubkey)
    message = rsa.decrypt(crypto, privkey)
    x, y = crypto, message
    lust_cr = []
    lust_cr.append(x)
    lust_cr.append(y)
    print(lust_cr[0])
    print(lust_cr[1])









