import datetime
import time
from selenium.webdriver.common.by import By
from rost_final_params import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

""" Позитивные тесты авторизации с временной меткой.
В случае удачи создается скриншот. В случае провала создается запись в результирующий файл."""

# python -m pytest -v --driver Chrome --driver-path chromedriver.exe rost_fin.py
now = datetime.datetime.now()
time_file = now.strftime("%y_%m_%d_%H_%M_%S")

"""Тест авторизации по телефону"""


def test_form_auth_tel(selenium):
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
    time.sleep(5)
    result_h1 = WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.XPATH, '// *[ @ id = "app"] / main[1] / div[1] / div[2] / div[3] / h3[1]')))
    if result_h1:
        selenium.save_screenshot(f'{time_file}result_tel_auth_PASSED.png')
    else:
        with open('report_FAILED.txt', 'a+') as result:
            result.write('Тест авторизации по номеру телефона провален.\nВремя {}'.format(now))
            result.close()
        raise Exception("login tel error")


"""Тест авторизации по email"""


def test_form_auth_email(selenium):
    selenium.get(base_url)
    find_auth_email = WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="t-btn-tab-mail"]')))
    find_auth_email.click()
    find_username_tel = WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.XPATH, "// *[ @ id = 'username']")))
    find_username_tel.clear()
    find_username_tel.send_keys(log_email)
    find_username_password = WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
    find_username_password.clear()
    find_username_password.send_keys(pass_rt)
    button_auth = WebDriverWait(selenium, 10).until(EC.presence_of_element_located((By.ID, 'kc-login')))
    button_auth.click()
    time.sleep(5)
    result_h1 = WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.XPATH, '// *[ @ id = "app"] / main[1] / div[1] / div[2] / div[3] / h3[1]')))
    if result_h1:
        selenium.save_screenshot(f'{time_file}result_email_auth_PASSED.png')
    else:
        with open('report_FAILED.txt', 'a+') as result:
            result.write('Тест авторизации по почтовому адресу провален.\nВремя {}'.format(now))
            result.close()
        raise Exception("login email error")


"""Тест авторизации по логину.
В качестве логина используем email"""


def test_form_auth_login(selenium):
    selenium.get(base_url)
    find_auth_login = WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="t-btn-tab-login"]')))
    find_auth_login.click()
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
    time.sleep(5)
    result_h1 = WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.XPATH, '// *[ @ id = "app"] / main[1] / div[1] / div[2] / div[3] / h3[1]')))
    if result_h1:
        selenium.save_screenshot(f'{time_file}result_tel_auth_login_PASSED.png')
    else:
        with open('report_FAILED.txt', 'a+') as result:
            result.write('Тест авторизации по логину провален.\nВремя {}'.format(now))
            result.close()
        raise Exception("login tel error")


""" Тест по лицевому счету отсутствует, из-за отсутствия каких либо услуг, предоставляемых мне провайдером. """
