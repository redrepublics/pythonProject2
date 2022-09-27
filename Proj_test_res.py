dict_func = ['+','-', ':']
while True:
    dict_func_res = input("Введите желаемое действие:\n Сложение  [+]\n Вычитание [-]\n Деление [:]\n")
    if dict_func_res not in dict_func[:]:
        print("Я так не могу. Попробуем снова.")
        continue
    else:
        break

a = int(input("Введите первое число:\n"))

while True:
    try:
        b = int(input("Введите второе число:\n"))
    except ValueError as except_print:
        print("Вы ввели некорректное значение.", except_print)
        print("Пробуем снова.")
        continue
    if b == 0 and dict_func_res in dict_func[2]:
        print("На 0 делить нелья! Попробуем снова.")
        continue
    else:
        break


def fun_plus(a,b):
    if dict_func_res in dict_func[0]:
        res = a+b
        return res
    elif dict_func_res in dict_func[1]:
        res = a-b
        return res
    elif dict_func_res in dict_func[2]:
        res = a/b
        return res
    else:
        return 0
print("Результат операции равен ", fun_plus(a,b))

# dict_sample = {"Company": "Toyota","model": "Premio","year": 2012}
# for k, v in dict_sample.items():
#     print(v)
