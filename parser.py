#код нацелен на папку запуска скрипта (сделать потом именно так перед конвертацией механизма
#посмотреть в py to exe, можно ли принтануть юзергайд
#если папки log нет, она там создается. Если есть, действие по всей схеме не происходит. Проработать этот момент.

#тут импортируем все модули
import os
import sys
import glob
import time
from datetime import datetime

#задаем уникальную переменную для файла вывода
now = datetime.now()
current_time = now.strftime("%y_%m_%d_%H_%M_%S")
folder = os.getcwd()
pattern = '*.txt'


# with open(os.path.join('E:', 'test.txt'), 'rt', encoding="utf-8") as file:



#обрабатываем ошибку отсутствия нужного файла в нужной папке, иначе записываем файл, переименовываем его с временной
#меткой указанной выше, не забыв закрыть рабочие файлы, дабы не допустить утечку памяти при работе
def pars_def():
    try:
        with open(os.path.join(folder, 'new_file.txt'), 'rt',) as file:
            error_per = file.readlines()
    except FileNotFoundError:
        print(f"Запрашиваемый файл не найден")
# print(error_per)
    else:
        error_search = 'Error'
        final = "\n".join(s for s in error_per if error_search.lower() in s.lower())
        if final:
            my_result = open(os.path.join(folder, 'new_file.txt'), 'w', encoding="utf-8")
            my_result.write(final)
            print('Ошибки обнаружены и записаны.')
            my_result.close()
            file.close()
            old_file = os.path.join(folder, "new_file.txt")
            new_file = os.path.join(folder, f"aspo_error{current_time}.txt")
            os.rename(old_file, new_file)
        else:
            print('Ошибок нет')
            file.close()

