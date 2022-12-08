import sys
import requests


# Определяем кто и откуда звонил. Ввод из консоли.

class CallCLASS:
    def __init__(self):
        self.res_print = None
        self.api_key = '1VBGxnPGmXuApLfYlFGta0L17JQnN63u50xVAuYA'
        self.base_url = 'https://api.numlookupapi.com/v1/validate/'
        try:
            self.tel_number = int(input('Введите номер телефона, только цифры. Пример: 7921*******\nВВОД: '))
        except ValueError:
            print('Некорректный формат номера телефона.')
        else:
            pass
        try:
            self.request = requests.get(f'{self.base_url}+{self.tel_number}?apikey={self.api_key}')
        except AttributeError:
            print('Ошибка в запросе API. Возможно вы некорректно ввели номер телефона.')
            sys.exit(0)

    def information_by_number(self):
        self.res_print = self.request.json()
        if False != self.res_print['valid']:
            print('Нахождение номера: ', (self.res_print['location']))
            print('Страна: ', self.res_print['country_name'])
            if self.res_print['carrier']:
                print('Оператор: ', self.res_print['carrier'])
            print('Тип телефона: ', self.res_print['line_type'])
        else:
            print('По данному номеру телефона получить информацию нельзя.')


result = CallCLASS()
result.information_by_number()
