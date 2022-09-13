# допустим, у нас есть список, содержащий первые 4 буквы латинского алфавита
letters = ['a', 'b', 'c', 'd']
# с помощью метода append() мы добавляем ещё один элемент в список
letters.append('Z')
print(letters)
print(len(letters))
print(letters[len(letters)-1])
letters.append('f') # добавляем ещё одну букву
letters.append('g') # и ещё одну

print(letters[len(letters)-1])


L = ["а", "б", "в", 1, 2, 3, 4]
print (L[1:4])
# ["б", "в", 1]

L = ["а", "б", "в", 1, 2, 3, 4]
print (L[::3])
# ["а", 1, 4]
L = ["а", "б", "в", 1, 2, 3, 4]
print(len(L))
#7
print (L[-4::-1])
# [1, "в", "б", "а"]
L = ["а", "б", "в", 1, 2, 3, 4]
print (L[6:3:-1])
# [4, 3, 2]


# имеем список с числами с плавающей точкой
L = [3.3, 4.4, 5.5, 6.6]
# печатаем сам объект map
print(map(round, L)) # к каждому элементу применяем функцию округления
# <map object at 0x7fd7e86eb6a0>
# и результат его преобразования в список
print(list(map(round, L)))
# [3, 4, 6, 7]
print()
string = input("Введите числа через пробел:")
list_of_strings = string.split() # список строковых представлений чисел
list_of_numbers = list(map(int, list_of_strings)) # список чисел
print(sum(list_of_numbers[::3])) # sum() вычисляет сумму элементов списка
#1 1 2 3 5 8 13 21 34 55