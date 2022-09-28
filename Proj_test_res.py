import math
import gc
#базовый список значаний, добавляем по надобности разработки, не забыв дополнить математику
dict_func = ['+','-', ':', '*', '^']
#start обработки ввода переменных
#обработка на неправильный параметр, деление на ноль etc
def run():
    print("status on")
    while True:
        dict_func_res = input("Введите желаемое действие:\n Сложение  [+]\n Вычитание [-]\n Деление [:]\n Умножение [*]\n Возведение в степень [^]\n")
        if dict_func_res not in dict_func[:]:
            print("Вы ввели некорректное значение.")
            continue
        else:
            break

    while True:
        try:
            a = int(input("Введите первое число:\n"))
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
        nod = input('Будем считать снова? \n Для продолжения введите "да", для завершения - любой символ.\n')
        if nod != 'да':
            print("status off")
            i = 0
            import gc
            gc.collect()
            break
        else:
            run()
    else:
        print("Что-то пошло не так")


