from datetime import datetime
from decorators import do_twice


def my_decorator(func):
    def wrapper():
        print("Начало выполнения функции.")
        value_hour = datetime.now().hour
        if 9 <= datetime.now().hour < 18:
            print('Выполняем функцию в рабочее время.')
            print(f'Сейчас {value_hour} часов')
            func()
        else:
            print('Время отдыха, функцию не выполняем.')
            print(f'Сейчас {value_hour} часов')
        print("Конец выполнения функции.")

    return wrapper


@my_decorator
def my_first_decorator():
    print("Это мой первый декоратор!")


@do_twice
def t_twice():
    print("Это вызов функции t_twice!")


my_first_decorator()
t_twice()

