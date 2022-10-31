import os
import sys
import time

from db_tools_params import get_folder


def test_folder():
    x = os.access(get_folder()[0], os.W_OK)
    if x is True:
        print('Указанный каталог существует. Доступ на чтение и запись есть.')
        pass
    else:
        print('Указанный каталог не существует, либо у вас нет прав.\n'
              'Программа прекратит выполнение через 10 секунд.')
        t_time()
        sys.exit(1)


def t_time():
    n = 10
    while True:
        print(n, ' ', end='')
        time.sleep(1)
        n = n - 1
        if n == 0:
            break



