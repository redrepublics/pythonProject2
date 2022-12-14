#возможно предусмотреть максимальное время игры
#задаем переменные и импортируем библиотеки
import random
from random import randint
from datetime import datetime
import time

#переменные условия игры
num_ranodom_min, num_ranodom_max = 1, 10
count_c, count_c_max, =  num_ranodom_min, 3
num_random = randint(num_ranodom_min, num_ranodom_max)
num_random_ave = num_ranodom_max / 2
#даем id игрока по имени, для возможной интеграции куда-то
username_game = input("Давайте познакомимся. Как Вас зовут? ")
if not username_game:
    username_game = 'Аноним'

#начало интерактива
print(f"""\033[34m\nПриветствую вас {username_game}!
Давайте поиграем в игру,'Убеги от горного тролля'.
На пути у Вас дверь с волшебным замком. Замок заколдован.
Gamemaster подскзаывает: {username_game}, назовите волшебное число от {num_ranodom_min} до {num_ranodom_max} и тогда вы спасетесь!
У вас всего {count_c_max} попытки, иначе тролль догонит вас и съест.\033[0m""")
#print(num_random) #для тестов

start_time = datetime.now()
#цикл с основными условиями
while True:
    try:
        num_user = int(input("Введите волшебное число: "))
    except ValueError as except_print:
        print(f"В игре можно использовать только целые числа, без запятой или точки!\nПопытка не засчитана.\n Попытка №{count_c}")
        continue
    if (num_user not in range(num_ranodom_min, num_ranodom_max+1)) and count_c != count_c_max:
        count_c += 1
        print(f"Ваше волшебное число не подходит к условиям игры!\nЧисла, доллжны быть, от {num_ranodom_min} до {num_ranodom_max}.\nПопытка №{count_c}")
        continue
    elif num_user != num_random and count_c < count_c_max:
        count_c += 1
        print(f"Увы,{username_game},но вы не угадали.\nПопытка №{count_c}.")
        if count_c == count_c_max and num_random <= num_random_ave:  # меньше или равно
            print("\033[34mGamemaster: Число может быть в первой части последовательности.\033[0m")
            continue
        elif count_c == count_c_max and num_random >= num_random_ave:  # больше или равно
            print("\033[34mGamemaster: Число может быть во второй части последовательности.\033[0m")
            continue
        continue
    elif num_user == num_random:
        print(f"\033[32m{username_game}, вы угадали! Ура! Дверь распахнулась и вы убежали от тролля.\033[0m")
        if count_c == num_ranodom_min:
            print(f"Ваше звание БОЛЬШОЙ МОЛОДЕЦ! Вы угадали с {count_c} попытки.")
        elif count_c == num_ranodom_min + 1:
            print(f"Ваше звание МОЛОДЕЦ! Вы угадали со {count_c} попытки.")
        else:
            print(f"Вы угадали с {count_c} попытки.")
        break
    elif count_c == count_c_max:
        print(f"Вы проиграли {username_game}. Тролль догнал вас и ударил по голове кулаком. Волшебная цифра была {num_random}.")
        break
    else:
        print("Что-то пошло не так.")

print(f"""\nНемного статистики, {username_game}:
Использовано количество ходов {count_c} из {count_c_max} возможных.
Игровое время заняло {datetime.now() - start_time}.""")