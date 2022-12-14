L = ["а", "б", "в", 1, 2, 3, 4]
print (L[1:4])
# ["б", "в", 1]


L = ["а", "б", "в", 1, 2, 3, 4]

print (L[::3])
# ["а", 1, 4]

L = ["а", "б", "в", 1, 2, 3, 4]
print (L[3::-1])
# [1, "в", "б", "а"]

L = ["а", "б", "в", 1, 2, 3, 4]
print (L[6:3:-1])
# [4, 3, 2]

string = input("Введите числа через пробел:")
list_of_strings = string.split() # список строковых представлений чисел
list_of_numbers = list(map(int, list_of_strings)) # список чисел
print(sum(list_of_numbers[::3])) # sum() вычисляет сумму элементов списка
#1 1 2 3 5 8 13 21 34 55

