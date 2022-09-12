numbers_1 = '1 2 3 4 5 6 7'
print(numbers_1)
numbers_1_split = numbers_1.split()
print(numbers_1.split())


colors = 'red green blue'
colors_split = colors.split() # список цветов по отдельности
print(colors.split())
colors_joined = ' and '.join(colors_split) # объединение строк
print(colors_joined)
# red and green and blue

numb= '1 2 3 4 5 6 7'
print(numb)
print(numb[0])
print(numb[2])
print(numb[4])
print(numb[6])
print(numb[8])
print(numb[10])
print(numb[12])



#numbers = input("Введите числа через пробел:")

#numbers_split = numbers.split()
#numbers_lines = "\n".join(numbers_split)

#print(numbers_lines)

print()
age = input("Введите возраст:")
my_age = "Вам " + str(age) + " лет"
print(my_age)
