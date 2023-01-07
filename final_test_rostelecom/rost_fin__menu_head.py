import datetime
import time
from selenium.webdriver.common.by import By
from rost_final_params import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from rost_del_report import del_old_report

# Эта процедура удаляет все старые png. Старым считаем все что уже было в папке.
del_old_report()

# python -m pytest -v --driver Chrome --driver-path chromedriver.exe rost_fin__menu_head.py
now = datetime.datetime.now()
time_file = now.strftime("%y_%m_%d_%H_%M_%S")

"""Тест корректности переходов по двум пунктам меню, попарное тестирование."""


def test_menu_one(selenium):
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
    find_logo_link_for_my = WebDriverWait(selenium, 15).until(EC.presence_of_element_located((By.XPATH, '//*['
                                                                                                        '@id="root'
                                                                                                        '"]/div['
                                                                                                        '1]/div['
                                                                                                        '1]/div['
                                                                                                        '1]/div['
                                                                                                        '1]/div['
                                                                                                        '1]/div['
                                                                                                        '2]/div['
                                                                                                        '1]/div[1]/p['
                                                                                                        '1]')))
    find_logo_link_for_my.click()
    result = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, 'cards-title')))
    if result:
        selenium.save_screenshot(f'{time_file}result_menu_one_PASSED.png')
    else:
        with open('report_FAILED.txt', 'a+') as result:
            result.write('Тест перехода в раздел ДЛЯ МЕНЯ провален.\nВремя {}'.format(now))
            result.close()
        raise Exception("link error")


def test_for_business(selenium):
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
    find_logo_link_for_my = WebDriverWait(selenium, 15).until(EC.presence_of_element_located((By.XPATH, '//*['
                                                                                                        '@id="root'
                                                                                                        '"]/div['
                                                                                                        '1]/div['
                                                                                                        '1]/div['
                                                                                                        '1]/div['
                                                                                                        '1]/div['
                                                                                                        '1]/div['
                                                                                                        '2]/div['
                                                                                                        '1]/div[2]/p['
                                                                                                        '1]')))
    find_logo_link_for_my.click()
    time.sleep(10)
    result = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="paragraph--id'
                                                                                         '--1041"]/div[1]/div[2]/div['
                                                                                         '1]/div[1]/h2[1]')))
    if result:
        selenium.save_screenshot(f'{time_file}result_for_business_PASSED.png')
    else:
        with open('report_FAILED.txt', 'a+') as result:
            result.write('Тест перехода в раздел ДЛЯ БИЗНЕСА провален.\nВремя {}'.format(now))
            result.close()
        raise Exception("link error")
