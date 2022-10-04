#ниверсальный кросплатформенный парсер текстовых файлов, ищет событие по Error
#сливает несколько файлов из фоормата xml в txt, после получения результата возвращает все как было
import os,glob,time
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%y_%m_%d_%H_%M_%S")
folder = os.getcwd()
ver = '1.0.0.3 alfa'
format_start = '.xml'
format_finish = '.txt'
name_data_file = 'test.txt'
log_test_final = 'log_test_final.txt'
test_xml = 'test.xml'

def folder_dir():
    for filename in os.listdir(folder):
        infilename = os.path.join(folder, filename)
        if not os.path.isfile(infilename):
            continue
        else:
            oldbase = os.path.splitext(filename)
            newname = infilename.replace(format_start, format_finish)
            output = os.rename(infilename, newname)

def folder_dir_return():
    for filename in os.listdir(folder):
        infilename = os.path.join(folder, filename)
        if not os.path.isfile(infilename):
            continue
        else:
            oldbase = os.path.splitext(filename)
            newname = infilename.replace(format_finish, format_start)
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

#блок старта парсера, с временной задержкой

print(f"""{ver}.
Не выключайте парсер. По окончанию работ он выключиться самостоятельно 
и выгрузит результирущий файл формата aspo_error(время создания файла).rtf
в положив его в ту папку откуда был запущен.""")
print('Этап конвертации данных запущен.')
folder_dir()
time.sleep(10)
print("""Этап формирования блока для анализа запущен.
Чем больше файлов для анализа, тем больше времени
займет этот процесс.""")
files_sum()
time.sleep(10)
print('Идет анализ данных.')
try:
    with open(os.path.join(folder, name_data_file), 'rt',) as file:
        error_per = file.readlines()
except FileNotFoundError:
    print('Нет файла для работы')
else:
    error_search = 'Error' or 'error'
    final = "\n".join(s for s in error_per if error_search.lower() in s.lower())
    if final:
        my_result = open(os.path.join(folder, log_test_final), 'w')#, encoding="utf-8")
        my_result.write(final)
        print('Ошибки обнаружены и записаны.')
        my_result.close()
        file.close()
        encodings_files = open(os.path.join(folder, log_test_final), 'w', encoding="Windows-1251")
        encodings_files.close()
        old_file = os.path.join(folder, log_test_final)
        new_file = os.path.join(folder, f"aspo_error{current_time}.rtf")
        os.rename(old_file, new_file)
        folder_dir_return()
        os.remove(os.path.join(folder, test_xml))
    else:
        print('Ошибок нет')
