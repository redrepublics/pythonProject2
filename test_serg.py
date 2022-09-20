import datetime
now = datetime.datetime.now()
year_stop = (now.year-1)
print ("Сейчас мы расчитаем все високосные года, от вашего рождления до текущего года!")
while True:
    year_start = int(input("Введите год рождения.\n"))
    if year_stop <= year_start:
        print("Вы ввели текущий год, или смотрите в будущее.")
        print("Пробуем снова.")
        continue
    else:
        break
for i in range(year_start, year_stop+1):
    if i %400 ==0 or i %100 and i %4 !=0:
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