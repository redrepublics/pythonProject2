import os
import pyodbc
from ping_params import *


hostname = []
# hostname = ['8.8.8.8']
conn = pyodbc.connect('DRIVER={'+get_folder()[0]+'};SERVER='+get_folder()[1]+';DATABASE='+get_folder()[2]+';UID=' +get_folder()[3]+';PWD='+get_folder()[4]+';',autocommit=True)
cursor = conn.cursor()

cursor.execute('select IPAddress from tNodesDetails')
for row in cursor:
    x = ",".join(row)
    hostname.append(x)

for i in hostname:
    i = str(i)
    print(f'{i}')
    # response = os.system("ping -c 1 " + i)
    response = os.system(f'ping {i} > nul')
    if response == 0:
        print('Успех')
        with open("ping_on.txt", 'w+') as file:
            file.write(f'Доступен: {i}')
    else:
        print('Провал')
        with open('ping_off.txt', 'w+') as file:
            file.write(f'Не доступен: {i}')

cursor.close()
