from datetime import datetime
from ping3 import ping, verbose_ping


def text_text(func):
    print('Вывод функции декоратора - start')
    start = datetime.now()
    func()
    stop = datetime.now()
    print('Время выполнения', stop - start)
    print('Вывод функции декоратора - stop', '\n')


@text_text
def t_test():
    if ping('ya.ru') is False:
        print('Вывод функции t_test')
        print(False)
    else:
        print('Вывод функции t_test')
        print(True)


def two_params():
    return 2


def one_params(x):
    y = x - 2
    if y == 0:
        print('Вывод функции one_params')
        return True
    else:
        print('Вывод функции one_params')
        return False


print(one_params(two_params()))
