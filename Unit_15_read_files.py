import os
import time
from datetime import datetime


with open(os.path.join('E:', 'python_read_file.txt'), 'rt', encoding="utf-8") as file:
    text_error = 'Error'
    lines = file.readlines()
    for line in text_error:
        print("Мы нашли ошику")
        my_result = open(os.path.join('E:', 'log.txt'), 'w+', encoding="utf-8")
        my_result.write(line)


# print(my_file.readlines())

# my_file = open('E:\python_test1.txt','w', encoding="utf-8")
# my_file.write('тестовый тест')
# print('!!!!!!!!!!!', file=my_file)
#
# my_file.close('E:\python_test1.txt')