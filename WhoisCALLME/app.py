import random


# Вариант класса с циклом рандомно-го числа и передаче по классу параметра
class SetNUM(object):
    def __init__(self):
        self.my_num = (random.randrange(1, 11))
        self.random_num = (int(input('Введите число от 1 до 10: ')))

    def guess_the_number(self):
        print("Рандом {0}. Ваше число {1}".format(self.random_num, self.my_num))
        if self.random_num >= 6:
            print('Число во второй части последовательности')
        elif self.random_num <= 4:
            print('Число в первой части последовательности')
        elif self.random_num == 5:
            print('Число посередине последовательности')
        else:
            pass

        if self.random_num == self.my_num:
            print('Уры, вы угадали.')
        elif self.random_num < self.my_num:
            print('Ваше число больше загаданного')
        elif self.random_num > self.my_num:
            print('Ваше число меньше загаданного')
        else:
            pass


result = SetNUM()
result.guess_the_number()
