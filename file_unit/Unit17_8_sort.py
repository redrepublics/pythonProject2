import random  # модуль, с помощью которого перемешиваем массив

# пусть имеем массив всего лишь из 9 элементов
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
#
#
# is_sort = False  # станет True, если отсортирован
# count = 0  # счетчик количества перестановок
#
# while not is_sort:  # пока не отсортирован
#     count += 1  # прибавляем 1 к счётчику
#
#     random.shuffle(array)  # перемешиваем массив
#
#     # проверяем, отсортирован ли
#     is_sort = True
#     for i in range(len(array) - 1):
#         if array[i] > array[i + 1]:
#             is_sort = False
#             break
#
# print(array)
# print(count)

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
count = 0
for i in range(len(array)):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(array)):
        count += 1
        if array[j] < array[idx_min]:
            idx_min = j
    if i != idx_min:  # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_min] = array[idx_min], array[i]


print(array)
print(count)

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
count = 0

for i in range(len(array)):  # проходим по всему массиву
    idx_max = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(array)):
        count += 1
        if array[j] > array[idx_max]:
            idx_max = j
    if i != idx_max:  # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_max] = array[idx_max], array[i]

print(array)
print(count)