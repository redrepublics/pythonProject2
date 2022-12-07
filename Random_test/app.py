import random


def num_class():
    random_num = (random.randrange(1, 11))
    my_num = (int(input('Введите число от 1 до 10: ')))
    return random_num, my_num


def guess_the_number():
    a, b = num_class()
    print("Рандом {0}. Ваше число {1}".format(a, b))
    if a >= 6:
        print('Число во второй части последовательности')
    elif a <= 4:
        print('Число в первой части последовательности')
    elif a == 5:
        print('Число посередине последовательности')
    if a == b:
        print('Уры, вы угадали.')
    elif a < b:
        print('Ваше число больше загаданного')
    elif a > b:
        print('Ваше число меньше загаданного')


guess_the_number()
