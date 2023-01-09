import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
email = 'redrepublics@yandex.ru'


def valid_email():
    if re.fullmatch(regex, email):
        print("Valid email - {}".format(email))
    else:
        print("Invalid email - {}".format(email))


valid_email()
