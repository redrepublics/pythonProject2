import datetime
import itertools

from selenium.webdriver.common.by import By
from rost_final_params import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from rost_del_report import del_old_report

# python -m pytest -v --driver Chrome --driver-path chromedriver.exe rost_fin_usability.py

"""Тут парсим корректный лог авторизации. Если время не совпадает с выводом пусть даже на минуту, валим тест.
Иначе делам скиншот."""


def test_history_of_actions(selenium):
    now = datetime.datetime.now()
    time_file = now.strftime("%H:%M")
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
    result_h1 = WebDriverWait(selenium, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        'div#app > main > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div > div > span:nth-of-type(2) > span'))).text

    list_time = []
    list_history: list[str] = [str(result_h1)]
    list_time.append(time_file)
    # with open('test.txt', 'a+') as f:
    #     f.write(str(list_time))
    #     f.write('-----')
    #     f.write(str(list_history))
    #     f.close()
    x = 'сегодня в '.join(i for i in list_history if not i.isalpha())
    x_result_time = x[10:15]
    y = "'".join(i for i in list_time if not i.isalpha())
    if x_result_time in y:
        find_reg = WebDriverWait(selenium, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div#app > main > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div > div > span:nth-of-type(2) > span")))
        selenium.save_screenshot('result_tel_auth_PASSED.png')
    else:
        raise Exception("login history error")