a = {1, 2, 3, 4, 5, 6, 7, 8}
b = {2, 4, 6, 8, 10, 12}
a_set, b_set = set(a), set(b) # используем множественное присваивание
a_and_b = a_set.symmetric_difference(b_set)
print(a_and_b)




#a = set(input("Вводим первое множества"))
#b = set(input("Вводим первое множества"))
#a_set, b_set = set(a), set(b)
#a_and_b = a.symmetric_difference(b)
#print (a_and_b)

int_list = []
for element in input("Вводим первую последовательность ").split():
    int_list.append(int(element))
int_list2 = []
for element in input("Вводим вторую последовательность").split():
    int_list2.append(int(element))
a_set, b_set = set(int_list), set(int_list2)
a_and_b = a_set.symmetric_difference(b_set)
print(a_and_b)