#
# обрабатывать ошибки при неправильных параметрах в ini - реализовать
#
import pyodbc, os, os.path, shutil, time, sys
from SqlToolsClass import Request
from DriverClass import GetDriver, UsSelect, GetServer, GetDataBase, GetTimeSleep, GetMyDir, GetRV, GetFolder, GetBackUp, check_backup, mk_dir_new, FileError
from GetConnectSQL import GetConnectionString
file_ver = 'ver.sql'



def ConnectSql():
    try:
        connection = pyodbc.connect(GetConnectionString(), autocommit=True)
    except pyodbc.OperationalError as err:
        err_report_one = 'Error: Ошибка подключения к SQL Server.'
        err_report_two = ('ms-sql Operation Error: {0}'.format(err))
        with open(os.path.join(GetFolder(), FileError()), 'w+') as result:
            result.write(r'' + err_report_one + '\n' + err_report_two + '')
            result.close()
        print(f"Выполнение будет остановлено. {err_report_one},\n{err_report_two}")
        sys.exit(1)

    else:
        dbCursor = connection.cursor()

    while True:
        global request_user
        try:
            request_user = int(input("""МЕНЮ:
Запрос в tUserDetails............[1]
Узнать версию сервера MS SQL.....[2]
Узнать версию базы АСПО..........[3]
Выход............................[4]\n"""))
        except ValueError or NameError as err:
            print('Я так не умею.')
            err_report_all = ('Ошибка ввода пункта меню: {0}'.format(err))
            with open(os.path.join(GetFolder(), FileError()), 'w+') as result:
                result.write(r'' + err_report_all + '\n''')
                result.close()
            continue
        if request_user is UsSelect()[0]:
            dbCursor.execute(Request1.Get_RequestString())
            connection.commit()
            for respond_sql in dbCursor:
                print(respond_sql)
                print("")
            continue
        elif request_user is UsSelect()[1]:
            dbCursor.execute(Request2.Get_RequestString())
            connection.commit()
            for respond_sql in dbCursor:
                print(respond_sql)
                print("")
            continue
        elif request_user is UsSelect()[3]:
            print("Работа завершена.")
            break
#выполняем скрипт sql, предварительно читая его из файла
        elif request_user is UsSelect()[2]:
            with open(file_ver, 'r', encoding='utf-8') as sql_file:
                result_iterator = dbCursor.execute(sql_file.read())
                sql_file.close()
                for respond_sql in result_iterator:
                    if GetRV() in respond_sql:
                        print(f"У вас последняя {respond_sql}")
                    else:
                        print(f"Версию можно обновить.\nПоследняя {GetRV()} ► Ваша: {respond_sql}")
                        print("► Делаем резервную копию базы данных.")
                        dbCursor.execute(Request3.Get_RequestString())
                        connection.commit()
                        connection.autocommit = True
                        time.sleep(GetTimeSleep())
                        mk_dir_new()
                        dbCursor.close()#закрываем работу с запросм, после выполнения.
                        print('► Идет копирование вновь созданной резервной копии.')
                        shutil.move(os.path.join(GetFolder(), GetBackUp()), os.path.join(GetFolder(), GetMyDir(), GetBackUp()))
                        result_bk = check_backup()
                        if result_bk is True:
                            print("► Запускаем обновление!")
                            break
                        else:
                            err_report_all = ('Ошибка выполнения. Нет резервной копии или она не создадась. Проверьте свои права в ОС.')
                            with open(os.path.join(GetFolder(), FileError()), 'w+') as result:
                                result.write(r'' + err_report_all + '\n''')
                                result.close()
                            print("► Обновление невозможно, сначала сделайте резервную копию.")
                            break

                    continue
                continue
        else:
            print('► Что-то пошло не так.')


#начало блока запросов
Request1 = Request('select top(10)*, LName from tUserDetails order by RecTime DESC')
Request2 = Request('select @@VERSION')
Request3 = Request(r"BACKUP DATABASE [" + GetDataBase() + "] TO  DISK = N'" + GetFolder() + "" + GetBackUp() + "'")

ConnectSql()








