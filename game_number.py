#задаем переменные и импортируем библиотеки
import random
from random import randint

num_random, count_c, count_c_max, = randint(1, 10), 1, 3

#начало интерактива
print(f"""Давайте поиграем в игру 'Убеги от горного тролля'.
На пути у Вас дверь с волшебным замком. Замок заколдован.
Gamemaster подскзаывает: Назовите волбешное число от 1 до 10 и тогда вы спасетесь!
У вас всего {count_c_max} попытки, иначе тролль догонит вас и съест.""")
#print (num_random) #для тестов

#цикл с основными условиями
while True:
    try:
        num_user = int(input("Введите волшебное число: "))
    except ValueError as except_print:
        print(f"В игре можно использовать только целые числа! Попытка не засчитана.\n Попытка №{count_c}")
        continue
    if (num_user > 10 or num_user < 1) and count_c != count_c_max:
        count_c += 1
        print(f"Ваше число не в диапазоне условий игры! Попытка не засчитана.\n Попытка №{count_c}")
        continue
    elif num_user != num_random and count_c < count_c_max:
        count_c += 1
        print(f"Не угадали.\nПопытка №{count_c}.")
        if count_c == 3 and num_random <= 5:  # меньше или равно
            print("\033[37mGamemaster: Число может быть в первой части последовательности.\033[0m")
            continue
        elif count_c == 3 and num_random >= 5:  # больше или равно
            print("\033[37mGamemaster: Число может быть во второй части последовательности.\033[0m")
            continue
        continue
    elif num_user == num_random:
        print("Вы угадали! Ура! Дверь распахнулась и вы убежали от тролля.")
        if count_c == 1:
            print("Ваше звание БОЛЬШОЙ МОЛОДЕЦ! Вы угадали с первой попытки.")
        elif count_c == 2:
            print("Ваше звание МОЛОДЕЦ! Вы угадали со второй попытки.")
        else:
            print("Вы угадали с третьей попытки.")
        break
    elif count_c == count_c_max:
        print(f"Вы проиграли. Тролль догнал вас и ударил по голове кулаком. Волшебная цифра была {num_random}.")
        break
    else:
        print("Что-то пошло не так.")


