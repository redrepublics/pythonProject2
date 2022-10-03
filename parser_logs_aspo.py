#код нацелен на папку запуска скрипта (сделать потом именно так перед конвертацией механизма
#посмотреть в py to exe, можно ли принтануть юзергайд
#если папки log нет, она там создается. Если есть, действие по всей схеме не происходит. Проработать этот момент.

import os
import glob
import time
from datetime import datetime
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%y_%m_%d_%H_%M_%S")
folder = os.getcwd()

# with open(os.path.join('E:', 'test.txt'), 'rt', encoding="utf-8") as file:

def folder_dir():
    for filename in os.listdir(folder):
        infilename = os.path.join(folder,filename)
        if not os.path.isfile(infilename):
            continue
        else:
            oldbase = os.path.splitext(filename)
            newname = infilename.replace('.xml', '.txt')
            output = os.rename(infilename, newname)

def folder_dir_return():
    for filename in os.listdir(folder):
        infilename = os.path.join(folder,filename)
        if not os.path.isfile(infilename):
            continue
        else:
            oldbase = os.path.splitext(filename)
            newname = infilename.replace('.txt', '.xml')
            output = os.rename(infilename, newname)

def files_sum():
    # каталог текстовых файлов
    # измените на свой
    path = folder
    # паттерн поиска файлов по расширению
    pattern = '*.txt'

    glob_path = os.path.join(path, pattern)
    list_files = glob.glob(glob_path)
    # расширение нового файла установим как '.txt'
    new_file = 'test.txt'

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
time.sleep(10)
files_sum()
time.sleep(10)
try:
    with open(os.path.join(folder, 'test.txt'), 'rt',) as file:
        error_per = file.readlines()
except FileNotFoundError:
    print('Нет файла для работы')
else:
    error_search = 'Error' or 'error'
    final = "\n".join(s for s in error_per if error_search.lower() in s.lower())
    if final:
        my_result = open(os.path.join(folder, 'log_test_final.txt'), 'w', encoding="utf-8")
        my_result.write(final)
        print('Ошибки обнаружены и записаны.')
        my_result.close()
        file.close()
        old_file = os.path.join(folder, "log_test_final.txt")
        new_file = os.path.join(folder, f"aspo_error{current_time}.rtf")
        os.rename(old_file, new_file)
        folder_dir_return()
    else:
        print('Ошибок нет')
