L = {1,2,3,4,5,5,7,8,8}
#b = set(L)
#print (b)
#b_list=list(b)
#print (b_list)
c = list(set(L))
print (c)

text = input("Введите текст:")
unique = list(set(text))
print("Количество уникальных символов: ", len(unique))

z = input("Сюда пишем текст: ")
z1 = list(set(z))#определяем уникальные символы и делаем список
print ("Уникальных символов получилось: ", len(z1))#len - длинна заданного объекта