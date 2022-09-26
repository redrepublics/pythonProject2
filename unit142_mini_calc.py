sum_vis = ['-','+', ':', '*', '1', '2']
z = input ("\033[31m Выберите действие:\n Вычитание [-] \n Cложение [+]\n Деление [/]\n Умножение [*]\n Получение корня [1]\n Возведение в степень [2]\n\033[0m")
a = int(input ("Введите первое число\n"))
b = int(input ("Введите второе число\n"))
z = str(z)
a = int(a)
b = int(b)
def my_minus(a, b):
    print (f"Получаем: {a} {sum_vis[0]} {b} = ", a+b)
def my_plus(a,b):
    print (f"Получаем: {a} {sum_vis[1]} {b} = ", a+b)
if z in sum_vis[0]:
    my_minus(a,b)
elif z in sum_vis[1]:
    my_plus(a,b)
else:
    print ("Что-то пошло не так")

