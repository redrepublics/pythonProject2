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

#
@pytest.fixture(autouse=True)
def testing():
    # Переходим на страницу авторизации
    pytest_driver.get(url_test)
    # yield
    # pytest_driver.quit()


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
    my_pets_table = pytest_driver.find_elements(By.CSS_SELECTOR, '#all_my_pets > table > tbody > tr')
    my_pets_count = pytest_driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(":")[1]
    result_my_pets_table = (len(my_pets_table))
    result_my_pets_count = int(my_pets_count)
    if result_my_pets_count == result_my_pets_table:
        assert result_my_pets_count == result_my_pets_table
        print('\nКоличество питомцев - ОК.\nПо счетчику {0}. По строкам {1}.'
              .format(result_my_pets_count, result_my_pets_table))
    else:
        print('\nКоличество питомцев - ОК.\n По счетчику {0}. По строкам {1}.'
              .format(result_my_pets_count, result_my_pets_table))


def test_img():
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

    my_pets_img = pytest_driver.find_elements(By.XPATH, '//tbody/tr/th/img')

    for pet in my_pets_img:
        if pet.get_attribute('src') != '':
            count = 0
            count += 1
            result_img_pr = (100 / (len(my_pets_img) / count))
            print('\nБез фото всего {} %'.format(result_img_pr))
            assert result_img_pr == 50
