from auth_page import AuthPage
import time


# из консоли python -m pytest -v --driver Chrome --driver-path chromedriver.exe  test_auth_page.py

def test_auth_page_bad(selenium):
    page = AuthPage(selenium)
    page.enter_email("email@gmail.com")
    page.enter_pass("pass")
    page.btn_click()

    # знак != или == будет зависеть от того, верные или неверные данные мы вводим
    assert page.get_relative_link() != '/all_pets', "login error"

    time.sleep(1)  # задержка для учебных целей


def test_auth_page_good(selenium):
    page = AuthPage(selenium)
    page.enter_email("test_user_1@mail.ru")
    page.enter_pass("daorliar")
    page.btn_click()

    # знак != или == будет зависеть от того, верные или неверные данные мы вводим
    assert page.get_relative_link() == '/all_pets'

    time.sleep(1)  # задержка для учебных целей
