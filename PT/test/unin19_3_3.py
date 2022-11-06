import requests

# params request
pet_id = 9223372036854290796
name = 'doggie'
status = 'available'

# get request
res = requests.get(f'https://petstore.swagger.io/v2/pet/{pet_id}', headers={'accept': 'application/json'})
if res.status_code == 200:
    print('Correct server response: ', res.status_code, '\n', res.json())
else:
    print('Incorrect server response: ', res.status_code, '\n', res.json())


# post request
res2 = requests.post(f'https://petstore.swagger.io/v2/pet/{pet_id}', headers={'accept': 'application/json'},
                     data=f'name={name}&status={status}')
if res2.status_code == 200:
    print('Correct server response: ', res2.status_code, '\n', res2.json())
else:
    print('Incorrect server response: ', res2.status_code, '\n', res2.json())

