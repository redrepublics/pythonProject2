import math
sum_vis = ['-','+', '/', '*', 'корень', 'степень']
while True:
    z = input("\033[31m Выберите действие:\n 0.Вычитание [-] \n 1.Cложение [+]\n 2.Деление [/]\n 3.Умножение [*]\n 4.Получение корня [корень]\n 5.Возведение в степень [степень]\n\033[0m")
    if z in sum_vis:
        break
    else:
        print("Я, кальукулятор молодой, и пока это не умею. Попробуем снова, из возможного.")
        continue
if z in sum_vis[0] and sum_vis [1] and sum_vis [2] and sum_vis [3]:
    a = int(input("Введите первое число\n"))
    b = int(input("Введите второе число\n"))
elif z in sum_vis[4]:
    a = int(input('Введите число для получения корня\n'))
    b = 0
elif z in sum_vis[5]:
    a = int(input("Введите число\n"))
    b = int(input("Введите степень возведения\n"))
else:
    print()
z = str(z)
a = int(a)
b = int(b)
def my_step (a,b):
    print(f"Получаем: {a} в степени {b} = ",a**b)
def my_mnog (a,b):
    print (f"Получаем: {a} {sum_vis[3]} {b} = ", a*b)
def my_del (a,b):
    print(f"Получаем: {a} {sum_vis[2]} {b} = ", a/b)
def my_cor (a):
    print(f"Получаем:корень из {a} = ", math.isqrt(a))
def my_minus(a, b):
    print (f"Получаем: {a} {sum_vis[0]} {b} = ", a-b)
def my_plus(a,b):
    print (f"Получаем: {a} {sum_vis[1]} {b} = ", a+b)

if z in sum_vis[0]:
    my_minus(a,b)
elif z in sum_vis[1]:
    my_plus(a,b)
elif z in sum_vis[2]:
    my_del(a, b)
elif z in sum_vis[3]:
    my_mnog(a, b)
elif z in sum_vis[4]:
    my_cor(a)
elif z in sum_vis[5]:
    my_step(a, b)



else:
    print ("Что-то пошло не так")

