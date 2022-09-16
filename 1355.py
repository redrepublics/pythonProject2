# Запишите условие, которое является истинным, когда только
# одно из чисел А, В и С меньше 45. Иногда проще записать все условия и не пытаться упростить их.
nume_one = int(input('Введите первое число\n'))
nume_two = int(input('Введите второе число\n'))
nume_tree = int(input('Введите третье число\n'))

if ((nume_one<45) and (nume_two>=45) and (nume_tree>=45)) or \
    ((nume_one>=45) and (nume_two>=45) and (nume_tree<45)) or \
    ((nume_one>=45) and (nume_two<45) and (nume_tree>=45)):
    print ("Тут есть число меньше 45")
else:
    print("Числа меньше 45 нет, или их несколько")

