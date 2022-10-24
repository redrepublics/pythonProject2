from DriverClass import GetDriver, GetServer, GetDataBase

def GetConnectionString():
    connectionString = ("Driver={" + GetDriver() + "};" "Server=" + GetServer() + ";" "Database=" + GetDataBase() + ";" "Trusted_Connection=yes;")
    return connectionString

class Request:
    def __init__(self, requestString):
        self.requestString = requestString

    def Get_RequestString(self):
        return self.requestString






