# def lacl_test(base):
#     if base % 2 == 0:
#         print("Четное число")
#     else:
#         print("Нечетное число")
# while True:
#     try:
#         lacl_test(int(input("Введите число, для определения, четное оно или нет:\n")))
#     except ValueError as ve:
#         print("Ошибочный параметр. Нужно ввести только целые числа.")
#         print("Попробуем снова.")
#         continue
#     else:
#         break

def fin_coount (a,b):
    if a>b:
        count = a-b
    elif a<b:
        count = a+b
    else:
        count = 0


    return count
n1 = int(input())
n2 = int(input())
def_num = fin_coount(n1,n2)
print(def_num)
