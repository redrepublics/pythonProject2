from DB_tools_class import get_folder
from datetime import datetime

now = datetime.now()
# TODAY = now.strftime("%y_%m_%d_%H_%M_%S")
TODAY = now.strftime("%M_%S")
file_name_bak = f'{get_folder()[3]}{TODAY}'
bak_res = f'{file_name_bak}.bak'
print(bak_res)


Request1 = "SELECT @@version;"
Request2 = 'select * from tLocalParams'
Request3 = 'BACKUP DATABASE [' + get_folder()[3] + "] TO DISK = N'" + get_folder()[0] + "/" + get_folder()[3] + '-' + TODAY + ".bak'" # рабочий бэкап
# Request3 = 'BACKUP DATABASE [' + get_folder()[3] + "] TO DISK = N'" + get_folder()[0] + "/" + get_folder()[3] + '-' + TODAY + ".bak'" # рабочий бэкап
# Request3 = 'BACKUP DATABASE [' + get_folder()[3] + "] TO DISK = N'" + get_folder()[0] + "/" + get_folder()[3] + '-' + file_name_bak + '''' # рабочий бэкап
# Request4 = 'exec SP_DBREINDEX'
Request5 = 'DBCC SHRINKDATABASE ('+get_folder()[3]+', 10);' # рабочий шринк


req_1 = 'delete tRExamComplaints'
req_2 = 'delete tRemoteExams'
req_3 = 'delete tRemoteExamSignature'


