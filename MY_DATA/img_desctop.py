from PIL import Image, ImageDraw, ImageFont
import platform
from ip_data import *

print('*' * 10, 'Данные по ПК', '*' * 10)
print('Версия ОС', os.name, platform.system(), platform.release(), os_version)
print('Материнская плата: {0} {1} \nСерийный номер: {2}'.format(mb_serial_name.Manufacturer, mb_serial_name.Product,
                                                                mb_serial_name.SerialNumber))
print('Процессор: {0} {1} \nСерийный номер: {2}'.format(proc_info.Name, proc_info.SocketDesignation,
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


image = Image.open("2880x1800.jpg")
ram_text = round(system_ram)
font = ImageFont.truetype("arial.ttf", 25)
drawer = ImageDraw.Draw(image)

drawer.text((100, 100), f"Версия ОС, {os.name}, {platform.system()}, {platform.release()}, {os_version}",
            align='center',
            font=font, fill='white')
drawer.text((100, 130), f"Материнская плата: {mb_serial_name.Manufacturer} {mb_serial_name.Product} "
                         f"{mb_serial_name.SerialNumber}", align='left', font=font, fill='white')
drawer.text((100, 160), f"Процессор: {proc_info.Name} {proc_info.SocketDesignation} {proc_info.SerialNumber}",
            align='left', font=font, fill='white')
drawer.text((100, 190), f"Оперативная память: {ram_text} Гб", align='left', font=font, fill='white')



image.save('new_img.jpg')
image.show()
