import os
import sys
import win32api
import glob
import datetime

drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
now = datetime.datetime.now()
num = 0
err5 = 0
err2 = 0
format_files = 'log'


def dr_list():
    global num, err2, err5
    for i in range(len(drives)):
        for name in sorted(glob.glob(f'{drives[i]}/**/*.{format_files}', recursive=True)):
            try:
                os.remove(name)
                num += 1
            except PermissionError:
                err5 += 1
                pass
            except FileNotFoundError:
                err2 += 1
                pass
            else:
                pass
    now2 = datetime.datetime.now()
    print("Времени на поиск:", now2 - now)
    print('Поиск происходил по дискам', *drives, sep=', ')
    print('Всего файлов очищено:', num)
    print(f'Не удалось очистить WinError5: {err5}\n'
          f'Не удалось найти ранее обнаруженных файлов WinError2: {err2}')
    sys.exit(0)


dr_list()
