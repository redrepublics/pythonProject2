#импорт нужных для функционала библиотек
import os, glob, time, shutil
from datetime import datetime
from parserDef import GetIni
from GetParser import dir_cr, folder_dir, folder_dir_return
ver = '1.0.0.7 alfa'
#блок глобальных переменных
now = datetime.now()
current_time = now.strftime("%y_%m_%d_%H_%M_%S")
folder = os.getcwd()
init_list = ['test.txt', 'log_test_final.txt', 'test.xml', 'pars_result', '*.txt']
name_data_file = init_list[0]
log_test_final = init_list[1]
test_xml = init_list[2]
my_dir = init_list[3]
pattern = init_list[4]

#формирование результирующего файла
def files_sum():
    glob_path = os.path.join(folder, pattern)
    list_files = glob.glob(glob_path)
    # расширение нового файла установим как '.txt'
    new_file = name_data_file
    # чтение и запись
    if list_files:
        for file_name in list_files:
            # открываем файл из 'list_files' на чтение
            # а новый общий файл 'new_file' на дозапись
            with open(file_name, 'r') as fr, open(new_file, 'a') as fw:
                # дописываем строку с названием файла
                fw.write(f'\n\n---Запись найдена в файле {file_name}\n\n')
                # читаем данные построчно
                for line in fr:
                    # если нужно, то здесь обрабатываем каждую строку 'line'
                    # после обработки дописываем в общий файл
                    fw.write(line)

#блок старта парсера
print(f"""{ver}.
Не выключайте парсер. По окончанию работ он выключится самостоятельно 
и выгрузит результирущий файл формата aspo_error(время создания файла).txt
в положив его в папку pars_result, в корне запуска..""")
dir_cr()
print('Этап конвертации данных запущен.')
folder_dir()
time.sleep(1)
print("""Этап формирования блока для анализа запущен.
Чем больше файлов для анализа, тем больше времени займет этот процесс.""")
files_sum()
time.sleep(1)
print('Идет анализ данных.')
try:
    with open(os.path.join(folder, name_data_file), 'rt',) as file:
        error_per = file.readlines()
except FileNotFoundError:
    print('Нет файла для работы')
    time.sleep(5)
else:
    error_search_one = 'Error'
    error_search_two = 'Exception'
    error_search_three = GetIni()
    final_one = "\n".join(s for s in error_per if error_search_one.lower() in s.lower())
    final_two = "\n".join(s for s in error_per if error_search_two.lower() in s.lower())
    final_three = "\n".join(s for s in error_per if error_search_three.lower() in s.lower())

    if final_one or final_two or final_three:
        my_result = open(os.path.join(folder, log_test_final), 'w+')
        if final_one:
            my_result.write(r''+final_one+'\n')
        else:
            pass
        if final_two:
            my_result.write(r''+final_two+'\n')
        else:
            pass
        if final_three:
            my_result.write(r''+final_three+'\n')
        else:
            pass
        my_result.close()
        file.close()
        old_file = os.path.join(folder,  log_test_final)
        new_file = os.path.join(folder, f"aspo_error{current_time}.txt")
        os.rename(old_file, new_file)
        shutil.move(os.path.join(folder, new_file), os.path.join(folder, my_dir))
        folder_dir_return()
        os.remove(os.path.join(folder, test_xml))
        print('Ошибки обнаружены и записаны.')
        time.sleep(5)
    else:
        os.remove(os.path.join(folder, name_data_file))
        folder_dir_return()
        print('Ошибок не обнаружено.')
        time.sleep(5)
# окончание блока парсера

