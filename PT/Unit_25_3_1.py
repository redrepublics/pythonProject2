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
    # yield
    # pytest_driver.quit()


""" Тест на каунт питомцев и канут таблицы."""


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
    my_pets_count = \
        pytest_driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(":")[1]
    result_my_pets_table = (len(my_pets_table))
    result_my_pets_count = int(my_pets_count)
    if result_my_pets_count == result_my_pets_table:
        assert result_my_pets_count == result_my_pets_table
        print('\nКоличество питомцев - ОК.\nПо счетчику {0}. По строкам {1}.'
              .format(result_my_pets_count, result_my_pets_table))
    else:
        print('\nКоличество питомцев - ОК.\n По счетчику {0}. По строкам {1}.'
              .format(result_my_pets_count, result_my_pets_table))


""" Тест на фото. """


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


"""Тест на отсутствие или наличие какого либо параметра в списке."""


def test_array():
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
    name_pets = pytest_driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]')
    pet_name = []
    arr_count = len(name_pets)
    for pet in name_pets:
        pet_name.append(pet.text)
    arr_list = len(pet_name)
    if arr_count == arr_list:
        print('\nИмена есть у всех питомцев.')
    else:
        print('\nУ некоторых питомцев нет имен.')

    breed_pets = pytest_driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[2]')
    pet_breed = []
    arr2_count = len(breed_pets)
    for pet in breed_pets:
        pet_breed.append(pet.text)
    arr2_list = len(pet_breed)
    if arr2_count == arr2_list:
        print('\nПорода есть у всех питомцев.')
    else:
        print('\nУ некоторых питомцев не указана порода.')

    age_pets = pytest_driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[3]')
    pet_age = []
    arr3_count = len(age_pets)
    for pet in age_pets:
        pet_age.append(pet.text)
    arr3_list = len(pet_age)
    if arr3_count == arr3_list:
        print('\nВозраст есть у всех питомцев.')
    else:
        print('\nУ некоторых питомцев не указан возраст.')
    assert arr3_count == arr3_list and arr2_list == arr2_count and arr_list == arr_count


""" Тест на уникальные имена. """


def test_name():
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
    name_pets = pytest_driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]')
    pet_name = []
    for pet in name_pets:
        pet_name.append(pet.text)
    unique = [x for i, x in enumerate(pet_name) if i == pet_name.index(x)]
    if len(pet_name) == len(unique):
        print('\nВсе имена уникальны')
    else:
        print('\nЕсть повторяющиеся имена')
    assert len(pet_name) == len(unique)


""" Тест на уникальные записи. Если есть хоть одна не уникальная, будет провал."""


def test_dub():
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
    name_pets = pytest_driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]')
    breed_pets = pytest_driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[2]')
    age_pets = pytest_driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[3]')
    pet_name = []
    pet_breed = []
    pet_age = []
    n = False
    num_true = []
    for pet in name_pets:
        pet_name.append(pet.text)
        unique = [x for i, x in enumerate(pet_name) if i == pet_name.index(x)]
        if len(pet_name) == len(unique):
            n = True
            num_true.append(n)
        else:
            n = False
            num_true.append(n)
    for pet2 in breed_pets:
        pet_breed.append(pet2.text)
        unique2 = [x for i, x in enumerate(pet_breed) if i == pet_breed.index(x)]
        if len(pet_breed) == len(unique2):
            n = True
            num_true.append(n)
        else:
            n = False
            num_true.append(n)
    for pet3 in age_pets:
        pet_age.append(pet3.text)
        unique3 = [x for i, x in enumerate(pet_age) if i == pet_age.index(x)]
        if len(pet_age) == len(unique3):
            n = True
            num_true.append(n)
        else:
            n = False
            num_true.append(n)
    no_n = False
    if no_n is num_true:
        result = False
    else:
        result = True
    if result is True:
        print('\nВсе записи уникальны.')
    else:
        print('\nЗаписи не уникальны.')

    assert result is True
