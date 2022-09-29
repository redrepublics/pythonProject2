#задаем переменные и импортируем библиотеки
import random
from random import randint
num_random = randint(1,10)
count_c = 1
#начало интерактива
print('Давайте поиграем в игру "Убеги от горного тролля".')
print('На пути у Вас дверь с волшебным замком. Замок заколдован.')
print('Gamemaster подскзаывает: Назовите волбешное число от 1 до 10 и тогда вы спасетесь!')
print('У вас всего 3 попытки, иначе тролль догонит вас и съест.')
#print (num_random) #для тестов

#цикл с основными условиями
while True:
    try:
        num_user = int(input("Введите волшебное число: "))
    except ValueError as except_print:
        print("В игре можно использовать только целые числа! Попытка не засчитана.")#, except_print
        print(f"Попытка №{count_c}")
        continue
    if (num_user > 10 or num_user < 1) and count_c != 3:
        count_c += 1
        print("Посмотрите подсказку Gamemaster-а. Вы напрасно потратили попытку. ")  # , except_print
        print(f"Попытка №{count_c}")
        continue
    elif num_user != num_random and count_c < 3:
        count_c += 1
        print("Не угадали.")
        print(f"Попытка №{count_c}")
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
    elif count_c == 3:
        print(f"Вы проиграли. Тролль догнал вас и ударил по голове кулаком. Волшебная цифра была {num_random}.")
        break
    else:
        print("Что-то пошло не так.")

# print (num_random)

