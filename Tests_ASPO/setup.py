import pyodbc
from datetime import date


# тут процедура переменной времени, понадобиться почти сразу
def time_return():
    current_date = date.today()
    d = f"'{current_date}'"
    return d


# переменные запросов, и сами запросы
select_count = 'select count(*) from'
# req_exams = f'{select_count} tExaminations where RecTime >= {time_return()}'
# req_exams_obd = f'{select_count} tDMOSCExams where RecTime >= {time_return()}'
# res_exams_server_from_obd = f'{select_count} tExaminations where  RecTime >= {time_return()} and ExamResultID != 5'

req_exams = f'{select_count} tExaminations'
req_exams_obd = f'{select_count} tDMOSCExams'
res_exams_server_from_obd = f'{select_count} tExaminations where  ExamResultID != 5'

# Все что сonn, то цепляем к базе данных. Всего три сущности
conn_tpr = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                          "Server=11.10.10.51;"
                          "Database=MGOK_688;"
                          "UID=sa;"
                          "PWD=daorliar;", autocommit=True)

conn_serv = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                           "Server=11.10.10.1\MSSQL19;"
                           "Database=MGOK_688_serv_pkr;"
                           "UID=sa;"
                           "PWD=daorliar;", autocommit=True)

conn_Obd = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                          "Server=11.10.10.1\MSSQL19;"
                          "Database=Obd;"
                          "UID=sa;"
                          "PWD=daorliar;", autocommit=True)


# Выводим канут для ТПР
def tpr_return():
    cursor_tpr = conn_tpr.cursor()
    cursor_tpr.execute(req_exams)
    for result in cursor_tpr:
        result_list = [result]
        tpr_result = str(result_list[0])
        s = tpr_result.replace(')', '')
        s1 = s.replace(", ", "")
        result_tpr = s1.replace('(', '')
        cursor_tpr.close()
        return int(result_tpr)


# Выводим канут по серварку для ТПР
def server_return():
    cursor_serv = conn_serv.cursor()
    cursor_serv.execute(req_exams)
    for result in cursor_serv:
        result_list = [result]
        tpr_result = str(result_list[0])
        s = tpr_result.replace(')', '')
        s1 = s.replace(", ", "")
        result_tpr = s1.replace('(', '')
        cursor_serv.close()
        return int(result_tpr)


# Выводим каунт по ОБД
def obd_return():
    cursor_obd = conn_Obd.cursor()
    cursor_obd.execute(req_exams_obd)
    for result in cursor_obd:
        result_list = [result]
        obd_result = str(result_list[0])
        s = obd_result.replace(')', '')
        s1 = s.replace(", ", "")
        result_obd = s1.replace('(', '')
        cursor_obd.close()
        return int(result_obd)


# Выводим каунт по серваку (с условием), для ОБД
def server_obd_return():
    cursor_serv = conn_serv.cursor()
    cursor_serv.execute(res_exams_server_from_obd)
    for result in cursor_serv:
        result_list = [result]
        serv_result = str(result_list[0])
        s = serv_result.replace(')', '')
        s1 = s.replace(", ", "")
        result_serv = s1.replace('(', '')
        cursor_serv.close()
        return int(result_serv)


# так как передает утила, а не транспорт, даем в допуск что какунт ОБД может оставать от сервака на 5 измерений
# если база большая, а сервеерное железно маломощное, цифру стоит увеличить
def approximately_equal():
    obd = obd_return()
    server = server_obd_return()
    test_res_ = server - obd
    if test_res_ < 5:
        return True
    else:
        return False
