#Впишите вместо знаков «?» операцию сравнения идентификаторов списков
#до и после обновления, чтобы программа распечатала True, если они равны, иначе — False.

shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
list_id_before = id(shopping_center[-1])

shopping_center[-1].append("Uniqlo")
list_id_after = id(shopping_center[-1])

print(list_id_before == list_id_after)