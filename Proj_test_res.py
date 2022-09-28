import math
#базовый список значаний, добавляем по надобности разработки, не забыв дополнить математику
dict_func = ['+','-', ':', '*', '^']
ver_1 = 0.2
#start обработки ввода переменных
#обработка на неправильный параметр, деление на ноль etc
def run():
    print("status on")
    print(f"v.{ver_1}")
    while True:
        dict_func_res = input("Введите желаемое действие:\n Сложение  [+]\n Вычитание [-]\n Деление [:]\n Умножение [*]\n Возведение в степень [^]\n")
        if dict_func_res not in dict_func[:]:
            print("Вы ввели некорректное значение.")
            continue
        else:
            break

    while True:
        try:
            a = float(input("Введите первое число:\n").replace(',', '.'))#меняем запятую на точку, раз уж решили выводить числа с плавающей точкой
        except ValueError as except_print:
            print("Вы ввели некорректное значение.", except_print)
            print("Пробуем снова.")
            continue
        if a == 0 and dict_func_res in dict_func[2]:
            print("Данное действие дает ответ 0. Попробуем снова.")
            continue
        elif a == 0 and dict_func_res in dict_func[3]:
            print("Данное действие дает ответ 0. Попробуем снова.")
            continue
        else:
            break

    while True:
        try:
            b = float(input("Введите второе число\n").replace(',', '.'))
        except ValueError as except_print:
            print("Вы ввели некорректное значение.", except_print)
            print("Пробуем снова.")
            continue
        if b == 0 and dict_func_res in dict_func[2]:
            print("На 0 делить нелья! Попробуем снова.")
            continue
        else:
            break

#fin обработки ввоода
#start математики (тут добавляем условия)

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
        elif dict_func_res in dict_func[3]:
            res = a*b
            return res
        elif dict_func_res in dict_func[4]:
            res = math.pow(a,b)
            return res
        else:
            return 0
#fin математики
#start читабельных принтов результата
    def print_res (dict_func_res):
        if dict_func_res in dict_func[0]:
            print (f"{a} + {b} = {fun_plus(a,b)}")
        elif dict_func_res in dict_func[1]:
            print (f"{a} - {b} = {fun_plus(a,b)}")
        elif dict_func_res in dict_func[2]:
            print (f"{a} : {b} = {fun_plus(a,b)}")
        elif dict_func_res in dict_func[3]:
            print (f"{a} * {b} = {fun_plus(a,b)}")
        elif dict_func_res in dict_func[4]:
            print (f"{a} в степени {b} = {fun_plus(a,b)}")
        else:
            print ("Что-то пошло не так.")
#fin

#вызов основной рабочей функции

    print_res(dict_func_res)

#проверяем, если счетчик i в нуле, то просто стартуем, если отличен от нуля, то после действия предлагаем повторить
#иначе выходим. С выходом обнуляем счетчик.
i = 0
while True:
    if i == 0:
        i += 1
        run()
    elif i != 0:
        nod = input('Будем считать снова? \n Для продолжения введите "д",\n для завершения - любой символ.\n')
#главное, чтобы была клавиша
        import gc
        nod = nod.lower()
        if nod != 'д' or 'l':
            print("status off")
            i = 0
            import gc
            gc.collect()
            break
        else:
            gc.collect()
            run()
    else:
        print("Что-то пошло не так")


