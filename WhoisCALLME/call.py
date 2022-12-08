import sys
import requests

"""По self.base_url_two ограничение по кол-ву запросов"""


class WhoisCALLME:
    def __init__(self):
        self.api_key = 'a97abf69faa1463a94632e84efc96168'
        self.api_key_two = '76231a226060b7c8fc282a478bbf3ed7'
        self.num = int(input('Ведите номер телефона (пример 7911*******):'))
        self.base_url = 'https://phonevalidation.abstractapi.com/'
        self.base_url_two = 'https://htmlweb.ru/geo/api.php'
        self.response = requests.get(f"{self.base_url}v1/?api_key={self.api_key}&phone=+{self.num}")
        self.res_old = requests.get(f'{self.base_url_two}?json&telcod={self.num}&api_key={self.api_key_two}')

    def result_ops(self):
        try:
            result = self.response.json()
        except requests.exceptions.JSONDecodeError:
            print('Вы ввели неправильный формат телефона.')
            sys.exit(0)
        try:
            result_2 = self.res_old.json()
        except requests.exceptions.JSONDecodeError:
            print('Вы ввели неправильный формат телефона.')
            sys.exit(0)
        if result_2 == result_2['error']:
            print('Количество запросов исчерпано. Некоторые данные будут недоступны.')
        print(result_2)
        print(self.response.status_code)
        print(self.res_old.status_code)
        print('Звонок совершен с номера телефона {0}, тип телефона {1}'
              .format((result['format']['local']), (result['type'])))
        try:
            print('Откуда звонок:', result_2['0']['name'], result_2['0']['country'])
        except KeyError:
            print('Данные по стране и городу для этого номера недоступны')
        try:
            print('Оператор', result_2['0']['oper'])
        except KeyError:
            print('Данные по оператору для этого номера недоступны')
        try:
            print('Возможное местонахождение абонента: Широта {0}, Долгота {1}'.format((result_2['0']['latitude']),
                                                                                       (result_2['0']['longitude'])))
        except KeyError:
            print('Данные по геолокации для этого номера недоступны')


res = WhoisCALLME()
res.result_ops()
