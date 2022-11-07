import requests
import json

# https://petfriends.skillfactory.ru/all_pets
# all params
# a98adb702ee0d69b617573022e5077882aaf84aff129cb6376db68ef
status = 'available'
base_url = 'https://petstore.swagger.io/v2/pet/'
res_b = requests.get(f"{base_url}findByStatus?status={status}", headers={'accept': "application/json"})

pet_dict = res_b.json()[0]
pet_id = pet_dict['id']
name = pet_dict['name']
headers_test = {'accept': 'application/json', 'content-type': 'application/json'}
data_test = {
    "id": 0,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "foll",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}


def api_res():
    api_key_url = 'https://petfriends.skillfactory.ru/api/key'
    email = 'mailo4@mail.ru'
    password = 'daorliar'
    api_key_get = requests.get(f'{api_key_url}', headers={'email': f'{email}', 'password': f'{password}'})
    api_list = api_key_get.json()["key"]
    api_key = api_list
    return api_key


class TestClass:
    # get request
    def test_get(self):
        res = requests.get(f'{base_url}{pet_id}', headers=headers_test)
        if res.status_code == 200:
            print('Correct server response for GET: ', res.status_code, '\n', res.json())
        else:
            print('Incorrect server response for GET: ', res.status_code, '\n', res.json())

    # post request
    def test_post(self):
        res2 = requests.post(f'{base_url}', headers=headers_test,
                             data=json.dumps(data_test, ensure_ascii=False))
        if res2.status_code == 200:
            print('Correct server response for POST: ', res2.status_code, '\n', res2.json())
        else:
            print('Incorrect server response POST: ', res2.status_code, '\n', res2.json())

    def test_put(self):
        res3 = requests.put(f'{base_url}', headers=headers_test,
                            data=json.dumps(data_test, ensure_ascii=False).encode('utf-8'))
        if res3.status_code == 200:
            print('Correct server response for PUT: ', res3.status_code, '\n', res3.json())
        else:
            print('Incorrect server response PUT: ', res3.status_code, '\n', res3.json())

    def test_del(self):
        res4 = requests.delete(f'{base_url}{pet_id}', headers=headers_test)
        if res4.status_code == 200:
            print('Correct server response for DELETE: ', res4.status_code, '\n', res4.json())
        else:
            print('Incorrect server response DELETE: ', res4.status_code, '\n', res4.json())
