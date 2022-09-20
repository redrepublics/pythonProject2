mon_you = int(input("Введите номер месяца в котором вы родились "))
if 5>= mon_you >=3:
    print("Весна!")
elif mon_you == 1 or (13 > mon_you >=11) or mon_you == 12:
    print("Зима")
elif 8>= mon_you >=6:
    print("Лето")
elif mon_you >=9 and mon_you <11:
    print("Осень")
else:
    print("Нет такого месяца")