import datetime
from DB_tools_class import get_folder


TODAY = datetime.date.today()
Request1 = "SELECT @@version;"
Request2 = 'select * from tLocalParams'
Request3 = 'BACKUP DATABASE [' + get_folder()[3] + "] TO DISK = N'" + get_folder()[0] + "/" + get_folder()[3] + '-' + str(TODAY) + ".bak'"
