# import pyodbc
#
# driver_id_list = pyodbc.drivers()
# driver_id = driver_id_list[3]
# print(driver_id_list)
# print(driver_id)
from pymssql import connect
server = r'ZVERDVD-OKOC0U9\SQLEXPRESS' # I've also tried MORGANT-PC\SQLEXPRESS and SQLEXPRESS2014
username = '.\sa'
password = 'daorliar'
master_database_name = 'srw_688'
port = 1433
server_args = {'host': server, 'user': username, 'password': password,
               'database': master_database_name, 'port': port} # I've tried having the first key be both host and server, because pymssql's docs are unclear on the difference.
master_database = connect(**server_args)

