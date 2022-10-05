import pyodbc


driver_id = pyodbc.drivers()
print(driver_id)
drever_id_sql = driver_id[1]
server= 'ZVERDVD-OKOC0U9\SQLEXPRESS'
database = 'srw_688'

def connect_sql():
    connectionString = ("Driver={"+drever_id_sql+"};" "Server="+server+";" "Database="+database+";" "Trusted_Connection=yes;")
    connection = pyodbc.connect(connectionString, autocommit=True)
    dbCursor = connection.cursor()
    requestString = ('select top(10)*, LName from tUserDetails order by RecTime DESC')
    requestString2 = ('select @@VERSION')
    dbCursor.execute(requestString)
    connection.commit()
    for respond_sql in dbCursor:
        print(respond_sql)

connect_sql()








