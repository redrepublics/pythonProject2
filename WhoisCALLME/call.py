import requests


class WhoisCALLME:
    def __init__(self):
        self.api_key = 'a97abf69faa1463a94632e84efc96168'
        self.num = int(input('Ведите номер телефона'))
        self.base_url = 'https://phonevalidation.abstractapi.com/'
        self.response = requests.get(f"{self.base_url}v1/?api_key={self.api_key}&phone=+{self.num}")

    def result_ops(self):
        result = self.response.json()
        print(self.response.status_code)
        print('Звонок совершен с номера телефона {0}, локация {1}, тип телефона {2}'
              .format((result['format']['local']), (result["country"]['name']), (result['type'])))


res = WhoisCALLME()
res.result_ops()