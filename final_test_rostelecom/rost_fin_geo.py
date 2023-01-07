import datetime
import time
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
    geo_res = WebDriverWait(selenium, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="block-b2cpanellichnykhkabinetoviligeo"]/div[1]/a[1]/i[1]/svg[1]/path[1]')))
    geo_res.click()
    time.sleep(10)
