import datetime # импорт новой библиотеки
now = datetime.datetime.now()
year_stop = now.year
print ("Сейчас мы рассчитаем все високосные года, от вашего рождения до текущего года!")
while True:
    try:
        year_start = int(input("Введите год рождения:\n"))
    except ValueError as except_print:
        print("Вы ввели некорректное значение  ")#, except_print)
        print("Пробуем снова.")
        continue
    if year_stop <= year_start or year_start == 0:
        print("Вы ввели текущий год, или смотрите в будущее.")
        print("Пробуем снова.")
        continue
    else:
        break
for i in range(year_start, year_stop+1):
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
        print(i, "- високосный год")
    else:
        print(i, "- не високосный год")



#
# lister_num = []
# for z in range(1,32,1):
#     lister_num.append(z)
#     lister_num_max = max(lister_num)
#     lister_num_min = min(lister_num)
# print(lister_num)
# print(lister_num_max)
# print(lister_num_min)
#
# # new_list = []
# # for i in range(10):
# #     new_list.append(i)
# # print(new_list)