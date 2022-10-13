from DriverClass import GetDriver, GetServer, GetDataBase

def GetConnectionString():
    connectionString = ("Driver={" + GetDriver() + "};" "Server=" + GetServer() + ";" "Database=" + GetDataBase() + ";" "Trusted_Connection=yes;")
    return connectionString








