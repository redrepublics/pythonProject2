import os
from selenium import webdriver
from rost_final_params import *

""" Выгружаем кукисы для анализа. """


class CookiesLOAD:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(base_url_all)
        self.driver.add_cookie({"name": "test1", "value": "cookie1"})
        self.driver.add_cookie({"name": "test2", "value": "cookie2"})

    def load_cookies(self):
        with open('cookies.pkl', 'a+') as file:
            file.write(str(self.driver.get_cookies()))
            file.close()
        if os.path.getsize('cookies.pkl') > 0:
            print(self.driver.get_cookies())
        else:
            print('cookies не выгружены')


CookiesLOAD().load_cookies()
