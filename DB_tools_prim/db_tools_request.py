from db_tools_params import *

Request1 = "SELECT @@version;"
Request2 = 'select * from tLocalParams'
Request3 = 'BACKUP DATABASE [' + get_folder()[3] + "] TO DISK = N'" + get_folder()[0] + "/" + get_folder()[
    3] + '-' + bak_res + "'"  # рабочий бэкап
Request5 = 'DBCC SHRINKDATABASE (' + get_folder()[3] + ', 10);'  # рабочий шринк

req_1 = 'delete tRExamComplaints'
req_2 = 'delete tRemoteExams'
req_3 = 'delete tRemoteExamSignature'