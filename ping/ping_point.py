import pyodbc
from ping_params import *
from ping3 import ping

# Подключаемся к серверу
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


# выявляем в списке все что с экземплярами, и убираем, делаем по ним отчет
for person in hostname:
    if row in person:
        hostname.remove(person)
        with open("Сомнительная запись.txt", 'w+') as file:
            file.write(f'{current_time} Проверить вручную: {person}\n')
    else:
        pass


# смотрим ответ по выводу
# надо проверить на английской версии OC
def ping_point():
    for i in hostname:
        i = str(i)
        ping(i)
        if ping(i):
            with open("Доступные_хосты.txt", 'w+') as file:
                file.write(f'{current_time} Доступен: {i}\n')
            if int(get_folder()[5]) == 1:
                print(f'{i} - Успех.')
            else:
                pass
        else:
            with open('Недоступные_хосты.txt', 'w+') as file:
                file.write(f'{current_time} Недоступен: {i}\n')
            if int(get_folder()[5]) == 1:
                print(f'{i} - Провал.')
            else:
                pass
    cursor.close()


ping_point()
