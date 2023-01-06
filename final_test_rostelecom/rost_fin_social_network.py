import datetime
from selenium.webdriver.common.by import By
from rost_final_params import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from rost_del_report import del_old_report

""" Позитивные тесты авторизации с временной меткой..
В случае удачи создается скриншот. В случае провала создается запись в результирующий файл."""

# python -m pytest -v --driver Chrome --driver-path chromedriver.exe rost_fin_social_network.py
now = datetime.datetime.now()
time_file = now.strftime("%y_%m_%d_%H_%M_%S")

# Эта процедура удаляет все старые png. Старым считаем все что уже было в папке.
del_old_report()

"""Обязательное условие - авторизация в искомых сетях"""
"""Тест авторизации по через Вконтакте"""


def test_auth_vk(selenium):
    selenium.get(base_url)
    vk_start = WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a#oidc_vk > svg > path')))
    vk_start.click()
    vk_button = WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div#oauth_wrap_content > div:nth-of-type(3) > div > div > '
                                                         'button')))
    vk_button.click()
    result_h1 = WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.XPATH, '// *[ @ id = "app"] / main[1] / div[1] / div[2] / div[3] / h3[1]')))
    if result_h1:
        selenium.save_screenshot(f'{time_file}result_VK_auth_PASSED.png')
    else:
        with open('report_FAILED.txt', 'a+') as result:
            result.write('Тест авторизации по социальной сети ВК провален.\nВремя {}'.format(now))
            result.close()
        raise Exception("login email error")


def test_auth_yandex(selenium):
    selenium.get(base_url)
    yandex_start = WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a#oidc_vk > svg > path')))
    yandex_start.click()
    vk_button = WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a#oidc_ya > svg')))
    vk_button.click()
    result_h1 = WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.XPATH, 'div#root > div > div > div:nth-of-type(2) > form > div > button')))
    if result_h1:
        selenium.save_screenshot(f'{time_file}result_VK_auth_PASSED.png')
    else:
        with open('report_FAILED.txt', 'a+') as result:
            result.write('Тест авторизации по социальной сети ВК провален.\nВремя {}'.format(now))
            result.close()
        raise Exception("login email error")