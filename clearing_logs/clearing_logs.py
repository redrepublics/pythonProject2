import os
import sys
import glob
import win32api
import datetime
import webbrowser


drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
now = datetime.datetime.now()
current_time = now.strftime("%y_%m_%d_%H_%M_%S")
num, err5, err2 = (0,) * 3
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
    with open(f'run_report.{format_files}', 'w+') as report:
        report.write(f'Времени на поиск: {now2 - now}\n')
        report.write(f'Поиск происходил по дискам: {drives}\n')
        report.write(f'Всего файлов очищено: {num}\n')
        report.write(f'Не удалось очистить WinError5: {err5}\n'
                     f'Не удалось найти ранее обнаруженных файлов WinError2: {err2}')
        report.close()
        webbrowser.open(f'run_report.{format_files}')
    sys.exit(0)


dr_list()
