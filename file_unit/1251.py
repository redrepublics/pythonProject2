a = input("Введите первую строку: ")
b = input("Введите вторую строку: ")

a_set, b_set = set(a), set(b) # используем множественное присваивание

a_and_b = a_set.symmetric_difference(b_set)

print(a_and_b)

#Введите целые числа: 1 2 3 4 5 6 7 8
#Введите целые числа: 2 4 6 8 10 12