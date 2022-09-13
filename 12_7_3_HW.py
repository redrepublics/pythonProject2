#В этом случае используется формула следующего вида:
#S = (P x I x t / K) / 100
#Обозначения:
#S – конечная сумма, полученная по завершению действия депозита;
#P – сумма изначально внесенная на депозит;
#I – размер % ставки (за год);
#t – кол-во дней начисления %;
#K – кол-во дней за год по календарю.

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму для вклада (цифры): "))
deposit1 = (money * per_cent['ТКБ'] * 1)/100
deposit2 = (money * per_cent['СКБ'] * 1)/100
deposit3 = (money * per_cent['ВТБ'] * 1)/100
deposit4 = (money * per_cent['СБЕР'] * 1)/100
list1 = [deposit1, deposit2, deposit3, deposit4]
max_number = max(list1)
inverse = [(value, key) for key, value in per_cent.items()]
max_per_cent = (max(inverse)[1])
print ("Общая статистика:","ТКБ:",deposit1,"СКБ:",deposit2,"ВТБ:",deposit3, "СБЕР:",deposit4)
print("Наибольший процент:", max_number, " предоставит банк",max_per_cent)




