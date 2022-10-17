from GetSort import GetArray, GetElem
array = GetArray()
element = GetElem()

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


def binary_search(array, element, left, right):
    if left > right:
        return print("Такого параметра в списке нет.")
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


print("Номер в списке", binary_search(array, element, 0, len(array)-1))
