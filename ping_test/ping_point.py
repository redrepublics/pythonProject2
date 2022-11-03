import os
import pyodbc
from ping_params import *

# Подключаемся к серверу
hostname = ['192.1.1.0']
conn = pyodbc.connect(
    'DRIVER={' + get_folder()[0] + '};SERVER=' + get_folder()[1] + ';DATABASE=' + get_folder()[2] + ';UID=' +
    get_folder()[3] + ';PWD=' + get_folder()[4] + ';', autocommit=True)
cursor = conn.cursor()
# делаем запрос на IP
cursor.execute('select IPAddress from tNodesDetails')
# причесываем IP и загоняем в список
for row in cursor:
    x = ",".join(row)
    hostname.append(x)

# перебираем список, в случае успеха в один файл, в случае провала в другой, попутно выводим в консоль, что и как
def ping_point():
    for i in hostname:
        i: str = i
        response = os.system(f'ping {i} > nul')
        if response == 0:
            print(f'{i}')
            print('Успех')
            with open("ping_success.txt", 'w+') as file:
                file.write(f'{current_time} Доступен: {i}\n')
        elif response != 0:
            print(f'{i}')
            print('Провал')
            with open('ping_failure.txt', 'w+') as file:
                file.write(f'{current_time} Не доступен: {i}\n')
        else:
            pass
    cursor.close()


ping_point()
