import sys
import time
import psutil

""" Проверяем запущена ли служба, выводим по ней информацию.
 Имя службы хранится в self.service_name."""


class ChSERVICE:
    def __init__(self):
        self.res_start_type = 'start_type'
        self.res_bin_path = 'binpath'
        self.service = None
        self.service_name = 'MSSQL$SQLEXPRESS'
        self.d_name = 'display_name'

    def checking_service(self):
        count = 0
        while True:
            try:
                self.service = psutil.win_service_get(self.service_name)
                self.service = self.service.as_dict()
            except Exception as err:
                print(str(err))
                return
            if self.service:
                # print(self.service)
                print("Служба {2} найдена.\nМестоположение службы: {0}.\nТип запуска: {1}".
                      format(self.service[self.res_bin_path], self.service[self.res_start_type],
                             self.service[self.d_name]))
                count += 1
                time.sleep(0)
                print(('-' * 10), 'Опрос №', count, '\n')
                if count == 10:
                    sys.exit(0)
                if self.service and self.service['status'] == 'running':
                    print('Служба запущена.')
                else:
                    print("Служба не запущена.")
            else:
                print("Такой службы нет.")


ChSERVICE().checking_service()
