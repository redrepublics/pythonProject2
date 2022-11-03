import os
import pyodbc

hostname = ['8.8.8.8']
conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=localhost;DATABASE=SRW_688;UID=sa;PWD=daorliar;',
                      autocommit=True)
cursor = conn.cursor()

cursor.execute('select IPAddress from tNodesDetails')
for row in cursor:
    x = ",".join(row)
    hostname.append(x)

for i in hostname:
    i = str(i)
    print(f'{i}')
    # response = os.system("ping -c 1 " + i)
    response = os.system(f'ping {i} > nul')
    if response == 0:
        print('Успех')
        with open("ping_on.txt", 'w+') as file:
            file.write(f'Доступен: {i}')
    else:
        print('Провал')
        with open('ping_off.txt', 'w+') as file:
            file.write(f'Не доступен: {i}')

cursor.close()
