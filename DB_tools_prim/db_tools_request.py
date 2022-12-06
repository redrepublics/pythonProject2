from db_tools_params import *

Request1 = "SELECT @@version;"
Request2 = 'select * from tLocalParams'
Request3 = 'BACKUP DATABASE [' + get_folder()[3] + "] TO DISK = N'" + get_folder()[0] + "/" + get_folder()[
    3] + '-' + bak_res + "'"  # рабочий бэкап
Request5 = 'DBCC SHRINKDATABASE (' + get_folder()[3] + ', 10);'  # рабочий шринк

req_1 = 'delete tRExamComplaints'
req_2 = 'delete tRemoteExams'
req_3 = 'delete tRemoteExamSignature'
req_5 = 'delete dtHubLog'
req_6 = 'delete tRemoteErrLog'
req_7 = 'delete tASUTJY'
req_8 = 'delete tASUTPersData'
req_9 = 'delete tASUTRouteList'
req_10 = 'delete tASUTFilters'
req_11 = 'delete tExamComplaints'
req_12 = 'delete tExamPhoto'
req_13 = 'delete tExamsPyro'
req_14 = 'delete tRExamComplaints'
req_15 = 'delete tRemoteCardInfo'
req_16 = 'delete tRemoteExamSignature'
req_17 = 'delete tSignatureJorn'
req_18 = 'delete tCurrentExams'
req_19 = 'delete tExamADParameters'
req_20 = 'delete tExamComplaints'
req_21 = 'delete tExamCalculated'
req_22 = 'delete tExamComplaints'
req_23 = 'delete tExamsBadConditions'
req_24 = 'delete tExamsHASH'
req_25 = 'delete dtEIDsForSend'
