from PIL import Image, ImageDraw, ImageFont
import platform
from ip_data import *
import ctypes
import os

# print('*' * 10, 'Данные по ПК', '*' * 10)
# print('Версия ОС', os.name, platform.system(), platform.release(), os_version)
# print('Материнская плата: {0} {1} \nСерийный номер: {2}'.format(mb_serial_name.Manufacturer, mb_serial_name.Product,
#                                                                 mb_serial_name.SerialNumber))
# print('Процессор: {0} {1} \nСерийный номер: {2}'.format(proc_info.Name, proc_info.SocketDesignation,
#                                                         proc_info.SerialNumber))
# print('Оперативная память: {0} GB'.format(system_ram))
# print('Видеокарта: {0} \nПоддерживаемое разрешение: {1}'.format(gpu_info.Name, gpu_info.VideoModeDescription))
#
# print('*' * 10, 'Данные для сети и подключения', '*' * 10)
# print('Имя учетной записи сеанса: {}'.format(my_name))
# print('Внешний IP: {}'.format(ip))
# print('IP адрес v4:', ip_v4)
# print('MAC адрес:', '-'.join(address[i:i + 2] for i in range(0, len(address), 2)))
# print('Сетевое имя ПК:', hostname)


def count_a():
    global count_avi
    result = []
    count_avi += 15
    axis_x: int = 500
    result.extend((axis_x, count_avi))
    return result


mbs = mb_serial_name
prc = proc_info
image = Image.open("start.jpg")
ram_text = round(system_ram)
font = ImageFont.truetype("arial.ttf", 25)
drawer = ImageDraw.Draw(image)
print_mac = str('-'.join(address[i:i + 2] for i in range(0, len(address), 2)))


def res_desktop():
    drawer.text((count_a()[0], count_a()[1]),
                f"Версия ОС {os.name}, {platform.system()}, {platform.release()}, {os_version}", align='center',
                font=font, fill='white')
    drawer.text((count_a()[0], count_a()[1]), f"Материнская плата: {mbs.Manufacturer} {mbs.Product} {mbs.SerialNumber}",
                align='left', font=font, fill='white')
    drawer.text((count_a()[0], count_a()[1]), f"Процессор: {prc.Name} {prc.SocketDesignation} {prc.SerialNumber}",
                align='left', font=font, fill='white')
    drawer.text((count_a()[0], count_a()[1]), f"Оперативная память: {ram_text} Гб", align='left', font=font,
                fill='white')
    drawer.text((count_a()[0], count_a()[1]), f"Видеокарта: {gpu_info.Name}, {gpu_info.VideoModeDescription}",
                align='left', font=font, fill='white')
    drawer.text((count_a()[0], count_a()[1]), "", align='left', font=font, fill='white')
    drawer.text((count_a()[0], count_a()[1]), f"Имя учетной записи сеанса:{my_name}", align='left', font=font,
                fill='white')
    drawer.text((count_a()[0], count_a()[1]), f"Внешний IP: {ip}", align='left', font=font, fill='white')
    drawer.text((count_a()[0], count_a()[1]), f"IP адрес v4: {ip_v4}", align='left', font=font, fill='white')
    drawer.text((count_a()[0], count_a()[1]), f"MAC адрес: {print_mac}", align='left', font=font, fill='white')
    drawer.text((count_a()[0], count_a()[1]), f"Сетевое имя ПК: {hostname}", align='left', font=font, fill='white')
    path = os.path.join(os.getcwd(), 'result.jpg')
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)


res_desktop()
