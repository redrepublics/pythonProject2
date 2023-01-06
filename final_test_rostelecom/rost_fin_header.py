import datetime
from selenium.webdriver.common.by import By
from rost_final_params import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from rost_del_report import del_old_report

# Эта процедура удаляет все старые png. Старым считаем все что уже было в папке.
del_old_report()

# python -m pytest -v --driver Chrome --driver-path chromedriver.exe rost_fin_header.py
now = datetime.datetime.now()
time_file = now.strftime("%y_%m_%d_%H_%M_%S")

"""Тест перехода по ссылка в шапке сайта, после авторизации."""


def test_form_main_site(selenium):
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
    main_site = WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a#rt-btn')))
    main_site.click()

    result_test = WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="cards-title"]/div[1]/h1[1]')))
    if result_test:
        selenium.save_screenshot(f'{time_file}result_main_site_PASSED.png')
    else:
        with open('report_FAILED.txt', 'a+') as result:
            result.write('Тест перехода из личного кабинета на основной сайт провален.\nВремя {}'.format(now))
            result.close()
        raise Exception("login tel error")
