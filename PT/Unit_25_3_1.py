import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

e_mail = 'test_user_1@mail.ru'
user_my = 'test_user_1'
pass_test = 'daorliar'
pytest_driver = webdriver.Chrome('chromedriver.exe')
url_test = 'http://petfriends.skillfactory.ru/login'
url_my_pets = 'https://petfriends.skillfactory.ru/my_pets'


@pytest.fixture(autouse=True)
def testing():
    # Переходим на страницу авторизации
    pytest_driver.get(url_test)
    yield
    pytest_driver.quit()


def test_show_my_pets():
    # Вводим email
    pytest_driver.find_element(By.ID, 'email').send_keys(e_mail)
    # Вводим пароль
    pytest_driver.find_element(By.ID, 'pass').send_keys(pass_test)
    # Нажимаем на кнопку входа в аккаунт
    pytest_driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    time.sleep(1)
    pytest_driver.find_element(By.CLASS_NAME, 'navbar-toggler-icon').click()
    time.sleep(1)
    pytest_driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
    time.sleep(1)
    assert pytest_driver.find_element(By.TAG_NAME, 'h2').text == user_my
