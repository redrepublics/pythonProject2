# def linear_solve(a, b):
#     return b/a
#
# print(linear_solve(2, 9))
# print(linear_solve(0,1))

# функция выводит дискриминант квадратного уравнения
# def D(a,b,c):
#     return b**2 - 4*a*c
yesno = input("""Введите Y, если хотите авторизоваться или N, 
             если хотите продолжить работу как анонимный пользователь: """)

auth = yesno == "Y"

def is_auth(func):
    def wrapper():
        if auth:
            print("Пользователь авторизован")
            func()
        else:
            print("Пользователь неавторизован. Функция выполнена не будет")
    return wrapper

@is_auth
def from_db():
    print("some data from database")

from_db()
print(a)