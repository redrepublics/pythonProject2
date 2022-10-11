s = "Hello"

print(s.find('l'))

print (s[::-1])
print(("Длинна строки равна:", len(s)))#длинна строки
print(s.isdigit()) # строка состоит из цифр?
print(s.isalpha()) # строка состоит из букв?
print(s.isalnum()) # строка состоит из цифр и букв?
print()
colors = 'red green blue'
colors_split = colors.split() # список цветов по отдельности
print(colors.split())
colors_joined = ' and '.join(colors_split) # объединение строк
print(colors_joined)
