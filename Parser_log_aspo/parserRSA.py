import rsa, os

folder = os.getcwd()
KeyParserAspo = b'17110367'
key_lust = []
key_lust.append(rsa.PublicKey(8611358230186391020299884467627008805631867422184296025775040113155292187404091008391828212109012111160193892945618249623785973404528075573378180488699411, 65537))
key_lust.append(rsa.PrivateKey(8611358230186391020299884467627008805631867422184296025775040113155292187404091008391828212109012111160193892945618249623785973404528075573378180488699411, 65537, 1785289596312655367087515911037248709005907848470604850728679524809511495531410086323245025094710056967296658966006870838551894074625906357076875122535305, 4976621894468449988039155076339535136070221736664167314792320432105946835123890807, 1730362163892333445841066415765865910608387667078479960761628212597781573))
pubkey, privkey = key_lust[0], key_lust[1]

def CriptoRSA():
    if KeyParserAspo:
    # блок создания нового файла по переменной KeyParserAspo
    # crypto = rsa.encrypt(KeyParserAspo, pubkey)
    #     with open(os.path.join(folder, 'validaspo.bin'), 'wb+') as result:
    #         result.write(rsa.encrypt(KeyParserAspo, pubkey))
    #         result.close()
        with open(os.path.join(folder, 'validaspo.bin'), 'rb') as result:
            content = result.read()
            message = rsa.decrypt(content, privkey)
            result.close()
            if message == KeyParserAspo:
                print("Валидация пройдена")
                RSAReturn = True
            else:
                print("Провал")
                RSAReturn = False
    return RSAReturn