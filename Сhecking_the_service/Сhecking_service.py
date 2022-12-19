import sys
import time
import psutil
from Сhecking_service_params import *


""" Проверяем запущена ли служба, выводим по ней информацию.
 Имя службы хранится в self.service_name."""


class ChSERVICE:
    def __init__(self):
        self.res_start_type = 'start_type'
        self.res_bin_path = 'binpath'
        self.service = None
        self.service_name = serv
        self.d_name = 'display_name'
        self.count = 0

    def checking_service(self):
        while True:
            try:
                self.service = psutil.win_service_get(self.service_name)
                self.service = self.service.as_dict()
            except Exception as err:
                print(str(err))
                with open('report.txt', 'a+') as file:
                    file.write(f'{self.service_name} not found\n')
                sys.exit(0)
            if self.service:
                print(('-' * 10), 'Опрос №', self.count + 1, '\n')
                # print(self.service)
                print("Служба {2} найдена.\nМестоположение службы: {0}.\nТип запуска: {1}".
                      format(self.service[self.res_bin_path], self.service[self.res_start_type],
                             self.service[self.d_name]))
                self.count += 1
                time.sleep(s_time)
                if self.count == count_m:
                    sys.exit(0)
                if self.service and self.service['status'] == 'running':
                    print('Служба запущена!')
                    time.sleep(s_time*60)
                else:
                    with open('report.txt', 'a+') as file:
                        file.write(f'{self.service_name} not started\n')
                    print("Служба не запущена!")
                    file.close()
                    sys.exit(0)
            else:
                print("Такой службы нет.")


ChSERVICE().checking_service()
