import pyodbc
from datetime import date

current_date = date.today()

req_exams = f'select count(*) from tExaminations where RecTime >= {current_date}'
req_exams_obd = f'select count(*) from tDMOSCExams where RecTime >= {current_date}'
res_exams_server_from_obd = f'select count(*) from tExaminations where RecTime >= {current_date} and ExamResultID != 5'

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


def tpr_return():
    cursor_tpr = conn_tpr.cursor()
    cursor_tpr.execute(req_exams)
    for result in cursor_tpr:
        result_list = [result]
        tpr_result = str(result_list[0])
        s = tpr_result.replace(')', '')
        s1 = s.replace(", ", "")
        result_tpr = s1.replace('(', '')
        return int(result_tpr)


def server_return():
    cursor_tpr = conn_serv.cursor()
    cursor_tpr.execute(req_exams)
    for result in cursor_tpr:
        result_list = [result]
        tpr_result = str(result_list[0])
        s = tpr_result.replace(')', '')
        s1 = s.replace(", ", "")
        result_tpr = s1.replace('(', '')
        return int(result_tpr)


def obd_return():
    cursor_obd = conn_Obd.cursor()
    cursor_obd.execute(req_exams_obd)
    for result in cursor_obd:
        result_list = [result]
        obd_result = str(result_list[0])
        s = obd_result.replace(')', '')
        s1 = s.replace(", ", "")
        result_obd = s1.replace('(', '')
        return int(result_obd)


def server_obd_return():
    cursor_serv = conn_serv.cursor()
    cursor_serv.execute(res_exams_server_from_obd)
    for result in cursor_serv:
        result_list = [result]
        serv_result = str(result_list[0])
        s = serv_result.replace(')', '')
        s1 = s.replace(", ", "")
        result_serv = s1.replace('(', '')
        return int(result_serv)


print(obd_return())
print(server_obd_return())
