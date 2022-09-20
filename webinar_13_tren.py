price_list = {'морковь':50, 'мясо':300, 'жижа для вейпа':400}
you_money = int(input("Введи ваш баланс для покупок\n"))
# you_money -= price_list['морковь']
# you_money -= price_list['мясо']
# you_money -= price_list['жижа для вейпа']
for i in price_list.values():#делаем цикл и обьявляем переменную i - values() все параметры из словаря
    you_money = you_money -i#вычитаем переменную из баланса, пока не закончится словарь
    print(i)
if you_money <= 0:
    print(f"Вы потратились.Ваш баланс равен, {you_money} руб.",)
else:
    print(f"У вас осталось, {you_money} руб.")