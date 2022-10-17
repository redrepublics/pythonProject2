element_list = list(range(1, 1000))
def GetArray():
    while True:
        elemet_pars = []
        global array
        try:
            array = [int(x) for x in input(f"Введите несколько чисел от {element_list[0]} до {element_list[-1]} в любом порядке, через пробел: ").split()]
        except ValueError:
            print("Введено не число. Попробуем снова.")
            continue
        if array:
            elemet_pars.append(array)
            elemet_pars_res = elemet_pars[0]
            result = all(x in element_list for x in elemet_pars_res)
            if result is True:
                return array
            else:
                print("Числа которые вы ввели, находятся вне диапазона, либо список слишком мал. Попробуем снова.")
            break
        else:
            print("Что-то пошло не так. Попробуем снова.")
            continue



def GetElem():
    while True:
        try:
            element = int(input(f"Введите число от {element_list[0]} до {element_list[-1]}: "))
        except ValueError:
            print("Введено не число. Попробуем снова.")
            continue
        if element not in range(element_list[0], element_list[-1]):
            print("Число которые вы ввели, находятся вне диапазона. ")
            break
        else:
            return element

