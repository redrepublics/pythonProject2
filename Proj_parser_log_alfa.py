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

def folder_dir():
    for filename in os.listdir(folder):
        infilename = os.path.join(folder, filename)
        if not os.path.isfile(infilename):
            continue
        else:
            oldbase = os.path.splitext(filename)
            newname = infilename.replace('.xml', '.txt')
            output = os.rename(infilename, newname)

def folder_dir_revers():
    for filename in os.listdir(folder):
        infilename = os.path.join(folder, filename)
        if not os.path.isfile(infilename):
            continue
        else:
            oldbase = os.path.splitext(filename)
            newname = infilename.replace('.txt', '.xml')
            output = os.rename(infilename, newname)


#обрабатываем ошибку отсутствия нужного файла в нужной папке, иначе записываем файл, переименовываем его с временной
#меткой указанной выше, не забыв закрыть рабочие файлы, дабы не допустить утечку памяти при работе
def pars_def():
    try:
        with open(os.path.join(folder, 'test.txt'), 'rt',) as file:
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

def folder_result():
    glob_path = os.path.join(path, pattern)
    list_files = glob.glob(glob_path)
    # расширение нового файла установим как '.all'
    new_file = 'new_file.txt'

    # чтение и запись
    if list_files:
        for file_name in list_files:
            # открываем файл из 'list_files' на чтение
            # а новый общий файл 'new_file' на дозапись
            with open(file_name, 'r') as fr, open(new_file, 'a') as fw:
                # дописываем строку с названием файла
                fw.write(f'\n\n------------ {file_name}\n\n')

                # читаем данные построчно
                for line in fr:
                    # если нужно, то здесь обрабатываем каждую строку 'line'
                    # после обработки дописываем в общий файл
                    fw.write(line)


folder_dir()
pars_def()
folder_result()
folder_dir_revers()