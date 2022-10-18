import glob
import os
import shutil
import time
from datetime import datetime

from GetParser import dir_cr, folder_dir, folder_dir_return
from parserDef import paramsini, depthini
from parserRSA import resc_rsa

# блок глобальных переменных
ver = ['1', '0', '0', '8', 'Release candidate']
# время сна по всему коду
ts = 3
now = datetime.now()
current_time = now.strftime("%y_%m_%d_%H_%M_%S")
folder = os.getcwd()
init_list = ['test.txt', 'log_test_final.txt', 'test.xml', 'pars_result', '*.txt']
name_data_file = init_list[0]
log_test_final = init_list[1]
test_xml = init_list[2]
my_dir = init_list[3]
pattern = init_list[4]
ErrParser_err = f'ErrParser{current_time}.err'


# формирование результирующего файла
def files_sum():
    glob_path = os.path.join(folder, pattern)
    list_files = glob.glob(glob_path)
    # расширение нового файла установим как '.txt'
    n_file = name_data_file
    # чтение и запись
    if list_files:
        for file_name in list_files:
            # открываем файл из 'list_files' на чтение, а новый общий файл 'new_file' на дозапись
            with open(file_name, 'r', encoding='utf-8') as fr, open(n_file, 'a', encoding='utf-8') as fw:
                # делаем разделение
                fw.write(f'\n\n---Блок принадлежит {file_name}\n\n')
                # читаем данные построчно
                for line in fr:
                    # если нужно, то здесь обрабатываем каждую строку 'line'
                    # после обработки дописываем в общий файл
                    fw.write(line)


# блок старта парсера

resc_rsa()
print('.'.join(map(str, ver)))
print(f"""Не выключайте парсер. По окончанию работ он выключится самостоятельно 
и выгрузит результирущий файл формата aspo_error(время создания файла).txt
в положив его в папку pars_result, в корне запуска.""", flush=True)
dir_cr()
print('Этап конвертации данных запущен.')
folder_dir()
time.sleep(ts)
print("""Этап формирования блока для анализа запущен.
Чем больше файлов для анализа, тем больше времени займет этот процесс.""", flush=True)
files_sum()
time.sleep(ts)
print('Идет анализ данных.', flush=True)
try:
    with open(os.path.join(folder, name_data_file), 'rt', encoding='utf-8') as file:
        error_per = file.readlines()
except FileNotFoundError:
    err_report = 'Нет файла для работы.'
    with open(os.path.join(folder, ErrParser_err), 'w+', encoding='utf-8') as rf:
        rf.write(r'' + err_report + '')
        rf.close()
        print(err_report, flush=True)
    time.sleep(ts)
else:
    error_search_one = 'Error'
    error_search_two = 'Exception'
    error_search_three = paramsini()
    final_one = "\n".join(s for s in error_per if error_search_one.lower() in s.lower())
    final_two = "\n".join(s for s in error_per if error_search_two.lower() in s.lower())
    final_three = "\n".join(s for s in error_per if error_search_three.lower() in s.lower())

    # 0 все, 1 Eror , 2 Exception, 3 ini

    if final_one or final_two or final_three:
        my_result = open(os.path.join(folder, log_test_final), 'w+', encoding='utf-8')
        if depthini() == 0:
            my_result.write(r'' + final_one + '\n')
        else:
            pass
        if depthini() == 1:
            my_result.write(r'' + final_two + '\n')
        else:
            pass
        if depthini() == 2:
            my_result.write(r'' + final_three + '\n')
        else:
            pass
        if depthini() == 3:
            my_result.write(r'' + final_one + '\n')
            my_result.write(r'' + final_two + '\n')
            my_result.write(r'' + final_three + '\n')
        else:
            pass

        my_result.close()
        file.close()
        old_file = os.path.join(folder, log_test_final)
        new_file = os.path.join(folder, f"aspo_error{current_time}.txt")
        os.rename(old_file, new_file)
        shutil.move(os.path.join(folder, new_file), os.path.join(folder, my_dir))
        folder_dir_return()
        os.remove(os.path.join(folder, test_xml))
        print('Ошибки обнаружены и записаны.', flush=True)
        time.sleep(ts)
    else:
        os.remove(os.path.join(folder, name_data_file))
        folder_dir_return()
        err_report = 'Ошибок не обнаружено.'
        with open(os.path.join(folder, ErrParser_err), 'w+', encoding='utf-8') as rf:
            rf.write(r'' + err_report + '')
            rf.close()
            print(err_report, flush=True)
        time.sleep(ts)
