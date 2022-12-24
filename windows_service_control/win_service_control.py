import ctypes
import sys
import os
import psutil

svc = 'MSSQL$SQLEXPRESS'
st = 0
stat_work = 'status'
stat_mod = 'running'
""" Остановка и запуск службы с правами администратора. Без ошибки 5 (отказано в доступе)."""


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def _start_stop_srv():
    service = psutil.win_service_get(svc)
    service = service.as_dict()

    if is_admin() and service[stat_work] not in stat_mod:
        os.system(f'net start {svc}')
        print(psutil.win_service_get(svc))
    elif is_admin() and service[stat_work] in stat_mod:
        os.system(f'net stop {svc}')
        print(psutil.win_service_get(svc))
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


_start_stop_srv()

