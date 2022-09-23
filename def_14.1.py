def lacl_test(base):
    if base % 2 == 0:
        print("Четное число")
    else:
        print("Нечетное число")
while True:
    try:
        lacl_test(int(input("Введите число, для определения, четное оно или нет:\n")))
    except ValueError as ve:
        print("Ошибочный параметр. Нужно ввести только целые числа.")
        print("Попробуем снова.")
        continue
    else:
        break






