import datetime
from datetime import timedelta
from rost_del_report import del_old_report
from rost_final_params import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Эта процедура удаляет все старые png. Старым считаем все что уже было в папке.
del_old_report()

# python -m pytest -v --driver Chrome --driver-path chromedriver.exe rost_fin_time_load_site.py
now = datetime.datetime.now()
time_file = now.strftime("%y_%m_%d_%H_%M_%S")


def test_time(selenium):
    selenium.get(base_url)
    find_reg = WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.XPATH, "// *[ @ id = 't-btn-tab-phone']")))
    find_reg.click()
    find_username_tel = WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.XPATH, "// *[ @ id = 'username']")))
    find_username_tel.clear()
    find_username_tel.send_keys(log_tel)
    find_username_password = WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
    find_username_password.clear()
    find_username_password.send_keys(pass_rt)
    button_auth = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, 'kc-login')))
    button_auth.click()
    start = datetime.datetime.now()
    res = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div/div["
                                                                                      "2]/div[1]/div[2]/div["
                                                                                      "2]/div/span[2]/span")))
    end = datetime.datetime.now()
    if res:
        result: list[timedelta] = [end - start]
        bad_time = datetime.timedelta(seconds=2)
        if bad_time < result[0]:
            selenium.save_screenshot(f'{time_file}result_test_time_PASSED.png')
        else:
            with open('report_FAILED.txt', 'a+') as result:
                result.write('Страница грузиться слишком долго. Установлен порог в 2 секунды.\nВремя {}'.format(now))
                result.close()
            raise Exception("bad time")
