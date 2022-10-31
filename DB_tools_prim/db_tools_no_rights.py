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
        print('Указанный каталог не существует, либо у вас нет прав.'
              'Программа прекратит выполнение через 10 секунд.')
        time.sleep(10)
        sys.exit(1)