from GetSort import GetArray, GetElem
array = GetArray()
element_list = list(range(1, 1000))

def merge_sort(array):  # "разделяй"
    if len(array) < 2:  # если кусок массива равен 2,
        return array[:]  # выходим из рекурсии
    else:
        middle = len(array) // 2  # ищем середину
        left = merge_sort(array[:middle])  # рекурсивно делим левую часть
        right = merge_sort(array[middle:])  # и правую
        return merge(left, right)  # выполняем слияние

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


print("Отсортированный по возрастанию список:", merge_sort(array))

element = GetElem()

def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

# def one_t_res():
#     while True:
#         if element not in merge_sort(array):
#             # print("Введенного элемента нет в списке")
#             break
#         else:
#             index = merge_sort(array).index(element)
#             print('Индекс числа', element, 'в отсроритрованном списке =', index)
#             # print("Число стоит между", index - 1, "и", index + 1)
#         break

print("Ваше число в неотсортированном списке №", binary_search(array, element, 0, len(array)-1))
