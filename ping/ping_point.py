import pyodbc
from ping_params import *
from subprocess import PIPE, Popen

# Подключаемся к серверу
hostname = ['8.8.8.8']
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


# смотрим ответ по выводу
# надо проверить на английской версии винды
def ping_point():
    for i in hostname:
        i = str(i)
        res = Popen(f"ping -n 1 {i}", shell=True, stdout=PIPE)
        out = str(res.communicate()[0].decode("CP866"))
        r1 = out.find("100% потерь")
        r2 = out.find("Превышен интервал ожидания для запроса")
        if (str(r1) == -1) and (str(r2) == -1):
            if int(get_folder()[5]) == 1:
                print(f'{i}')
                print("Связь есть!")
            with open("ping_success.txt", 'w+') as file:
                file.write(f'{current_time} Доступен: {i}\n')

        else:
            if int(get_folder()[5]) == 1:
                print(f'{i}')
                print("Хост недоступен!")
            with open('ping_failure.txt', 'w+') as file:
                file.write(f'{current_time} Не доступен: {i}\n')
    cursor.close()


ping_point()
