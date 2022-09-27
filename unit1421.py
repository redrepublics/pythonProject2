dict_func = ['+','-']
# dict_func_res = input("Введите желаемое действие:\n Сложение  [+]\n Вычитание [-]\n")
def res_key():
    while True:
        try:
            dict_func_res = input("Введите желаемое действие:\n Сложение  [+]\n Вычитание [-]\n")
        except ValueError as except_print:
            print("Вы ввели некорректное значение  ", except_print)
            print("Пробуем снова.")
            continue
        else:
            break

print(res_key())