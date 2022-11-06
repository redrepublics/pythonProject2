import requests
from datetime import datetime

status = 'available'
res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}",
                   headers={'accept': "application/json"})

now_start = datetime.now()
print('Выводим ответ:', res.text)
print('Выводим статус код:', res.status_code)
print('Выводим сам json:', res.json())
print('Смотрим тип отданного json:', type(res.json()))
now_stop = datetime.now()
res.close()
print('Времени на запрос:', now_stop - now_start)
#
# class TestRes:
#     def test_res(self):
#         status = 'available'
#         res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}",
#                            headers={'accept': "application/json"})
#         print(res.text)
#         print(res.status_code)
#         print(res.json())
#         print(type(res.json()))
#
#     def test_dict(self):
#         res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus", params={'status': 'available'},
#                            headers={'accept': 'application/json'})
#         print(res.text)
#         print(res.status_code)
