prod = input("Что ищем в холодильнике\n")
prod_hol = [["мясо"], ["колбаса", "сыр"],["виноград", "дыня", "сок"]]
for i in range(len(prod_hol)):
    for j in range(len(prod_hol[i])):
        if prod_hol[i][j] == prod:
            print(prod, "лежит на", i+1, "полке")
            break
    else:
        print("нет такого продукта на полке", i+1)
