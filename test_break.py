def lacl_test (base):

    while True:
        try:
        lacl_test(base)


    base == int(base)
    if base %2 == 0:
        print ("Четное число")

    else:
        print ("Нечетное число")


while True:
    try:
        lacl_test(int(input("Введите число, для определения, четное оно или нет\n")))
    except ValueError as ve:
        print("Неправильный параметр")
        break