import platform
from requests import get
import wmi
import os
import uuid
import socket

# Данные ПК
computer = wmi.WMI()
computer_info = computer.Win32_ComputerSystem()[0]
os_info = computer.Win32_OperatingSystem()[0]
proc_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()[0]
os_version = ' '.join([os_info.Version, os_info.BuildNumber])
system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB
mb_serial_name = computer.Win32_BaseBoard()[0]

# Данные сети
my_name = os.getlogin()
ip = get('https://api.ipify.org').content.decode('utf8')
address = hex(uuid.getnode())[2:]
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
my_address = socket.getaddrinfo(hostname, None)
ip_v4 = [item[4][0] for item in my_address if ':' not in item[4][0]][-1]

# Вывод информации, отсюда можно писать данные в файл

print('*' * 10, 'Данные по ПК', '*' * 10)
print('Версия ОС', os.name, platform.system(), platform.release(), os_version)
print('Материнская плата: {0} {1} Серийный номер: {2}'.format(mb_serial_name.Manufacturer, mb_serial_name.Product,
                                                              mb_serial_name.SerialNumber))
print('Процессор: {0} {1} Серийный номер: {2}'.format(proc_info.Name, proc_info.SocketDesignation,
                                                      proc_info.SerialNumber))
print('Оперативная память: {0} GB'.format(system_ram))
print('Видеокарта: {0} \nПоддерживаемое разрешение: {1}'.format(gpu_info.Name, gpu_info.VideoModeDescription))

print('*' * 10, 'Данные для сети и подключения', '*' * 10)
print('Имя учетной записи сеанса: {}'.format(my_name))
print('Внешний IP: {}'.format(ip))
print('IP адрес v4:', ip_v4)
print('MAC адрес:', '-'.join(address[i:i + 2] for i in range(0, len(address), 2)))
print('Сетевое имя ПК:', hostname)

# Сделать лог. В качестве имени файла использовать IP и имя ПК. Обработать IP заменив точки на нижние подчеркивания.
