# user_database = {'user':'password', 'iseedeadpeople': 'greedisgood','hesoyam': 'tgm'}
# key = input("Введите логин\n")
# value = input("Введите пароль\n")
# def dict_user_data():
#     if key in user_database.keys() and value in user_database.values():
#         return True
#     elif value not in user_database.values() or key not in user_database.keys():
#         return False
#     else:
#         return False
# fin_total = dict_user_data()
# if fin_total != True:
#      print("Вас нет в базе")
# else:
#      print("Вы в базе")

# Создайте функцию-генератор, возвращающую бесконечную последовательность натуральных чисел.
# По умолчанию, она начинается с единицы и шагом 1, но пользователь может указать любой шаг
# и любое число в качестве аргумента функции, с которого будет начинаться последовательность.


def count (start=0, step=1):
    counter = start
    while True:
        yield counter
        counter = counter + step

list_test=[]
for i in count():
    list_test.append(i)
    if i >=10:
        break
print(list_test)




