import pyodbc
from ping_params import *
from ping3 import ping
import sys
from ping_del_filese import file_old_del


# Подключаемся к серверу
# делаем запрос на IP, создаем список, убираем все лишнее, в том числе и экземпляры
def host_name():
    folder_txt()
    try:
        conn = pyodbc.connect(
            "DRIVER={" + get_folder()[0] + '};SERVER=' + get_folder()[1] + ';DATABASE=' + get_folder()[2] + ';UID=' +
            get_folder()[3] + ';PWD=' + get_folder()[4] + ';', autocommit=True)
    except pyodbc.OperationalError as err:
        err_report_one = 'Error: Ошибка подключения к SQL Server.'
        err_report_two = ('ms-sql Operation Error: {0}'.format(err))
        with open(os.path.join(os.getcwd(), 'отчеты', f'{current_time_file} Ошибка подключения.txt'), 'w+') as result:
            result.write(r'' + err_report_one + '\n' + err_report_two + '')
            result.close()
            print(f"Выполнение будет остановлено. {err_report_one},\n{err_report_two}")
            sys.exit(1)
    else:
        cursor = conn.cursor()
    cursor.execute('select IPAddress from tNodesDetails')
    for row in cursor:
        x = ",".join(row)
        hostname.append(x)
        for person in hostname:
            if del_t in person:
                hostname.remove(person)
                with open(os.path.join(os.getcwd(), 'отчеты', f"{current_time_file} Сомнительная запись.txt"),
                          'w+') as file:
                    file.write(f'{current_time} Проверить вручную: {person}\n')
                    file.close()
            else:
                pass
    cursor.close()
    return hostname


# смотрим ответ по выводу1
def ping_point():
    for i in host_name():
        i = str(i)
        ping(i)
        if ping(i):
            with open(os.path.join(os.getcwd(), 'отчеты', f"{current_time_file} Доступные_хосты.txt"), 'a') as file:
                file.write(f'{current_time} Доступен: {i}\n')
            if int(get_folder()[5]) == 1:
                print(f'{i} - Успех.')
            else:
                pass
        else:
            with open(os.path.join(os.getcwd(), 'отчеты', f"{current_time_file} Недоступные_хосты.txt"), 'a') as file:
                file.write(f'{current_time} Недоступен: {i}\n')
            if int(get_folder()[5]) == 1:
                print(f'{i} - Провал.')
            else:
                pass


file_old_del()
ping_point()
