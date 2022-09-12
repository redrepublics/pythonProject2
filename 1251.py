L = [1,1,2,3,2]
b = set(L)
b_list = list(b)
print(b_list)
# [1,2,3]!
text = input("Введите текст:")

unique = list(set(text))

print("Количество уникальных символов: ", len(unique))
