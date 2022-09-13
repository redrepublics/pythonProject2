# переприсваевам переменные int
a, b = -13, 7
print("а =", a, "b =", b)
print("")
a = a - b
print("а =", a)
b = a + b
print("b =", b)
a = b - a
print("а =", a)
# to and

# вывод нужных символов по порядку, нумерация всегда с 0
s = "python"
print(s[0:2])
# булевы значения
print(3 > 10)
# проверка символа в выволе
print('r' in 'world')
print(1.57 * 3 / 1.5 == 3.14)

# Кортеж
date = (1, 'january', 2020)
print(date[0])
print(date[1])
print(date[2])

s1, s2 = "Мак", " Дональдс"
s1 = s1 + s2
print(s1)

s4 = "foo"
print(id(s4), s4)  # проверяем идентификатор
s5 = "bar"
print(id(s5), s5)  # проверяем идентификатор
s4 = s4 + s5
print(id(s4), s4)  # проверяем идентификатор

