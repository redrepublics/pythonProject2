import time
from selenium.webdriver.common.by import By
from rost_final_params import *
import pytest

# python -m pytest -v --driver Chrome --driver-path chromedriver.exe rost_fin.py


def test_form_reg(selenium):
    selenium.get(base_url)
    time.sleep(5)
    find_reg = selenium.find_element(By.XPATH, "//*[@id='kc-register']")
    find_reg.click()
    time.sleep(5)