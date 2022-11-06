import requests


# headers = {'Accept': 'application/json', 'auth_key': 'a98adb702ee0d69b617573022e5077882aaf84aff129cb6376db68ef'}
# base_url = 'https://petfriends.skillfactory.ru/'
#
# # get all pets
# url = base_url + 'api/pets'
# params = {'filter': 'my_pets'}
#
# resp_b = requests.get(url, params=params, headers=headers)
status = 'available'
res_b = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}",
                   headers={'accept': "application/json"})
print(res_b.text)
print(res_b.json())
for row in res_b.json():
    # x = row['pets']['id']
    print(row)
    dict_pet = dict()
    # print(x)


# # params request
# pet_id = 12
# name = 'doggie'
# status = 'available'
# res_pet_id = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}",
#                           headers={'accept': "application/json"})
# # res_pet_id_text = dict(res_pet_id.text)
# print(res_pet_id.text)
# print(type(res_pet_id.text))
# print(res_pet_id.text[0])
#
# # api_key = requests.post('https://petfriends.skillfactory.ru/api/key', headers={'email': 'mailo4@mail.ru', 'password': 'daorliar'})
# # print(api_key.text)
#
#
#
#
# # get request
# res = requests.get(f'https://petstore.swagger.io/v2/pet/{pet_id}', headers={'accept': 'application/json'})
# if res.status_code == 200:
#     print('Correct server response: ', res.status_code, '\n', res.json())
# else:
#     print('Incorrect server response: ', res.status_code, '\n', res.json())
#
#
# # post request
# res2 = requests.post(f'https://petstore.swagger.io/v2/pet/{pet_id}', headers={'accept': 'application/json'},
#                      data=f'name={name}&status={status}')
# if res2.status_code == 200:
#     print('Correct server response: ', res2.status_code, '\n', res2.json())
# else:
#     print('Incorrect server response: ', res2.status_code, '\n', res2.json())
#
# # delete request
# # res3 = requests.delete()
