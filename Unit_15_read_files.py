import os
import time
from datetime import datetime
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%y_%m_%d_%H_%M_%S")


with open('python_read_file.txt', 'rt', encoding="utf-8") as file:
# with open(os.path.join('E:', 'python_read_file.txt'), 'rt', encoding="utf-8") as file:
    error_per = file.readlines()
    # print(error_per)
    error_search = 'Error'
    final = "\n".join(s for s in error_per if error_search.lower() in s.lower())
    if final:
        os.mkdir("logs")
        my_result = open('logs\log_test_final.txt', 'w', encoding="utf-8")
        my_result.write(final)
        print('Ошибки обнаружены и записаны.')
        my_result.close()
        file.close()
        old_file = os.path.join("E:", "log_test_final.txt")
        new_file = os.path.join("E:", f"aspo_error{current_time}.txt")
        os.rename(old_file, new_file)
    else:
        print('Ошибок нет')
        file.close()