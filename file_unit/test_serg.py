def hol():
    import datetime # импорт новой библиотеки
    now = datetime.datetime.now()
    year_stop = now.year
    year_vis = []
    year_not_vis = []
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
            year_vis.append(i)
        else:
            print(i, "- не високосный год")
            year_not_vis.append(i)
    if year_start == year_vis[0]:
        print(f"Вы родились в високосном году. Вы ввели {year_vis[0]}")
    else:
        print(f"Вы родились в не високосном году. Вы ввели {year_not_vis[0]}")
    print("Високосные года:", len(year_vis))
    print("Не високосные года:", len(year_not_vis))
    print("Вам", (len(year_vis)+len(year_not_vis)-1), "полных лет.")
hol()

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