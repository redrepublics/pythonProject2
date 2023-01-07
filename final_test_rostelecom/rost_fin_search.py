import datetime
import time
from selenium.webdriver.common.by import By
from rost_final_params import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from rost_del_report import del_old_report

# Эта процедура удаляет все старые png. Старым считаем все что уже было в папке.
del_old_report()

# python -m pytest -v --driver Chrome --driver-path chromedriver.exe rost_fin_search.py
now = datetime.datetime.now()
time_file = now.strftime("%y_%m_%d_%H_%M_%S")

""" Тест поиска по помощи. Внимание, для отсутствия наложения подтверждения геолокации, использовать в
selenium.set_window_size настройки экрана отличные от дефолтных для робота."""


def test_form_personal_account_search(selenium):
    selenium.set_window_size(1900, 1000)
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
    personal_account_link = WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="lk-btn"]')))
    personal_account_link.click()
    selenium.get(base_url_help)
    input_help = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                   '//*[@id="block'
                                                                                   '-b2spomoschformapoiskanastranicepomosch"]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]')))
    input_help.clear()
    input_help.send_keys('Подключение интернета')
    input_help_button = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                          '//*[@id="block'
                                                                                          '-b2spomoschformapoiskanastranicepomosch"]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]')))
    input_help_button.click()
    num_result = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#block'
                                                                                                    '-b2spomoschformapoiskanastranicerezultatovpoiska > div > div > div > div > div > div:nth-of-type(2) > span'))).text
    num_result_list = [num_result]
    y = "'".join(i for i in num_result_list if not i.isalpha())
    q = ''.join(i for i in y if not i.isalpha())
    if int(q) != 0:
        selenium.save_screenshot(f'{time_file}result_personal_account_search_PASSED.png')
    else:
        with open('report_FAILED.txt', 'a+') as result:
            result.write('Тест поиска в разделе ПОМОЩЬ провален.\nВремя {}'.format(now))
            result.close()
        raise Exception("search error")


