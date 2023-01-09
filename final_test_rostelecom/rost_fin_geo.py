import datetime
# import time
from selenium.webdriver.common.by import By
from rost_final_params import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from rost_del_report import del_old_report

# Эта процедура удаляет все старые png. Старым считаем все что уже было в папке.
del_old_report()

# python -m pytest -v --driver Chrome --driver-path chromedriver.exe rost_fin_geo.py
now = datetime.datetime.now()
time_file = now.strftime("%y_%m_%d_%H_%M_%S")

"""Тест правильных подсказок в меню изменения геопозиции"""


def test_changing_the_geo_position(selenium):
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
        EC.presence_of_element_located((By.XPATH, '//*[@id="rt-btn"]')))
    personal_account_link.click()
    geo_res = WebDriverWait(selenium, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div['
                                                                                          '1]/header/div[1]/div['
                                                                                          '1]/div/div[2]/div['
                                                                                          '5]/div/div/div[2]/div['
                                                                                          '3]/button[1]')))
    geo_res.click()
    geo_changing = WebDriverWait(selenium, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div['
                                                                                               '2]/div/div['
                                                                                               '1]/header/div[1]/div['
                                                                                               '3]/div/div['
                                                                                               '2]/div/div/div/a/span'
                                                                                     )))
    geo_changing.click()
    input_geo = WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="regionSearch"]')))
    input_geo.clear()
    input_geo.send_keys('Санкт')
    result = WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div['
                                                                                         '1]/header/div[1]/div['
                                                                                         '2]/div['
                                                                                         '2]/div/div/div/div/form/div'
                                                                                         '/div/ul/li[1]/div/span['
                                                                                         '1]'))).text
    if result == res_geo:
        selenium.save_screenshot(f'{time_file}result_changing_the_geo_position_PASSED.png')
    else:
        with open('report_FAILED.txt', 'a+') as result:
            result.write('Тест правильных подсказок в изменении геопозиции провален.\nВремя {}'.format(now))
            result.close()
        raise Exception("test changing_the_geo error")


""" Тест изменения геопозиции юзера"""


def test_changing_the_geo_position_msk(selenium):
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
        EC.presence_of_element_located((By.XPATH, '//*[@id="rt-btn"]')))
    personal_account_link.click()
    geo_res = WebDriverWait(selenium, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div['
                                                                                          '1]/header/div[1]/div['
                                                                                          '1]/div/div[2]/div['
                                                                                          '5]/div/div/div[2]/div['
                                                                                          '3]/button[1]')))
    geo_res.click()
    geo_changing = WebDriverWait(selenium, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div['
                                                                                               '2]/div/div['
                                                                                               '1]/header/div[1]/div['
                                                                                               '3]/div/div['
                                                                                               '2]/div/div/div/a/span'
                                                                                     )))
    geo_changing.click()
    input_geo = WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="regionSearch"]')))
    input_geo.clear()
    input_geo.send_keys(c_geo)
    input_geo_spb = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div['
                                                                                                '2]/div/div['
                                                                                                '1]/header/div['
                                                                                                '1]/div[2]/div['
                                                                                                '2]/div/div/div/div'
                                                                                                '/form/div/div/ul/li['
                                                                                                '1]')))
    input_geo_spb.click()
    geo_changing_res = WebDriverWait(selenium, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div['
                                                                                                   '2]/div/div/header'
                                                                                                   '/div[1]/div['
                                                                                                   '1]/div/div['
                                                                                                   '2]/div['
                                                                                                   '4]/div/div/div/a'
                                                                                         ))).text
    if geo_changing_res in c_geo:
        selenium.save_screenshot(f'{time_file}result_changing_the_geo_position_msk_PASSED.png')
    else:
        with open('report_FAILED.txt', 'a+') as result:
            result.write('Тест изменения геопозиции провален.\nВремя {}'.format(now))
            result.close()
        raise Exception("test changing_the_geo error")
