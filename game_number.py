#добавить список на осове рандома, вычислить число и дать его переменной для подсчета подсказки
#задаем переменные и импортируем библиотеки
import random
from random import randint

#переменные условия игры
num_ranodom_min, num_ranodom_max = 1, 10
count_c, count_c_max, =  1, 3
num_random = randint(num_ranodom_min, num_ranodom_max)
# def display():
#     xs = []
#     for i in range(9): # This is just to tell you how to create a list.
#         xs.append(i)
#     return xs


#начало интерактива
print(f"""Давайте поиграем в игру 'Убеги от горного тролля'.
На пути у Вас дверь с волшебным замком. Замок заколдован.
Gamemaster подскзаывает: Назовите волбешное число от {num_ranodom_min} до {num_ranodom_max} и тогда вы спасетесь!
У вас всего {count_c_max} попытки, иначе тролль догонит вас и съест.""")
#print (num_random) #для тестов

#цикл с основными условиями
while True:
    try:
        num_user = int(input("Введите волшебное число: "))
    except ValueError as except_print:
        print(f"В игре можно использовать только целые числа! Попытка не засчитана.\n Попытка №{count_c}")
        continue
    if (num_user not in range(num_ranodom_min, num_ranodom_max)) and count_c != count_c_max:
        count_c += 1
        print(f"Ваше число не в диапазоне условий игры!\n Попытка №{count_c}")
        continue
    elif num_user != num_random and count_c < count_c_max:
        count_c += 1
        print(f"Не угадали.\nПопытка №{count_c}.")
        if count_c == count_c_max and num_random <= 5:  # меньше или равно
            print("\033[37mGamemaster: Число может быть в первой части последовательности.\033[0m")
            continue
        elif count_c == count_c_max and num_random >= 5:  # больше или равно
            print("\033[37mGamemaster: Число может быть во второй части последовательности.\033[0m")
            continue
        continue
    elif num_user == num_random:
        print("Вы угадали! Ура! Дверь распахнулась и вы убежали от тролля.")
        if count_c == num_ranodom_min:
            print(f"Ваше звание БОЛЬШОЙ МОЛОДЕЦ! Вы угадали с {count_c} попытки.")
        elif count_c == num_ranodom_max - 1:
            print(f"Ваше звание МОЛОДЕЦ! Вы угадали со {count_c} попытки.")
        else:
            print(f"Вы угадали с {count_c} попытки.")
        break
    elif count_c == count_c_max:
        print(f"Вы проиграли. Тролль догнал вас и ударил по голове кулаком. Волшебная цифра была {num_random}.")
        break
    else:
        print("Что-то пошло не так.")


