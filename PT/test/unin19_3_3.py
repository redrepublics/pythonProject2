import requests

# all params
status = 'available'
base_url = 'https://petstore.swagger.io/v2/pet/'
api_key_url = 'https://petfriends.skillfactory.ru/api/key'
res_b = requests.get(f"{base_url}findByStatus?status={status}", headers={'accept': "application/json"})

pet_dict = res_b.json()[0]
pet_id = pet_dict['id']
name = pet_dict['name']

def api_res():
    email = 'mailo4@mail.ru'
    password = 'daorliar'
    api_key_get = requests.get(f'{api_key_url}', headers={'email': f'{email}', 'password': f'{password}'})
    api_list = api_key_get.json()["key"]
    api_key = api_list
    return api_key


class TestClass:
    # get request
    def test_get(self):
        res = requests.get(f'https://petstore.swagger.io/v2/pet/{pet_id}', headers={'accept': 'application/json'})
        if res.status_code == 200:
            print('Correct server response for GET: ', res.status_code, '\n', res.json())
        else:
            print('Incorrect server response for GET: ', res.status_code, '\n', res.json())

    # post request
    def test_post(self):
        res2 = requests.post(f'https://petstore.swagger.io/v2/pet/{pet_id}', headers={'accept': 'application/json'},
                             data=f'name={name}&status={status}')
        if res2.status_code == 200:
            print('Correct server response for POST: ', res2.status_code, '\n', res2.json())
        else:
            print('Incorrect server response Post: ', res2.status_code, '\n', res2.json())

# delete request
# res3 = requests.delete()
