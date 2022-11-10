from setup import *

# set DATEFORMAT YMD
""" Тут только положительные тесты.
Любой обвал теста - причина для создания таски.
Перед стартом лучше снести все старые тестовые данные, чтобы не было разночтений."""


def test_transfer_of_exams():
    """ Проверяем прохождение измерений между ТПР и сервер
    ТПР 11.10.10.51, Сервер 11.10.10.1
    Проект МГОК
    Делаем допуск + 1 измерение, для возможных таймаутов в передаче
    Запрос делаеться на день момента запуска теста, т.е. тестовые данные должны уже быть"""
    server, tpr = server_return(), tpr_return()
    assert tpr == server or tpr == (server + 1)


def test_serv_obd():
    """Провеоям проход данных с сервера на ТПР.
    Условия и каунты те же, с небольшим изменение по типу. Смотреть setup
    База ОБД живет на 11.10.10.1
    Даем больший допус по отставанию каунта измерений. Максимально что можем допустить это 5"""
    result = approximately_equal()
    assert True is result
