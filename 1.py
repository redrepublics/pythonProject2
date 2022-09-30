import random
from random import randint
num_random, count_c, count_c_max = randint(1, 10), 1, 3
def gamemaster():
    print("{Хотите подсказку от Gamemaster-а?")
    while True:
        try:
            help_gamemaster = input("Да [1], Нет - любой другой символ.")
        except ValueError as except_print:
            print("Ну нет, так нет.")
            break
        if help_gamemaster == '1' and num_random <= 5:#меньше или равно
            print("Gamemaster: Число может быть в первой части последовательности.")
            break
        elif help_gamemaster == '1' and num_random >= 5:#больше или равно
            print("Gamemaster: Число может быть во второй части последовательности.")
            break
        else:
            print("Ну нет, так нет.")
            break
gamemaster()

