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
# ip = get('https://api.ipify.org').content.decode('utf8')
address = hex(uuid.getnode())[2:]
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
my_address = socket.getaddrinfo(hostname, None)
ip_v4 = [item[4][0] for item in my_address if ':' not in item[4][0]][-2]
print(my_address)

# Вывод информации, отсюда можно писать данные в файл
count_avi: int = 100

