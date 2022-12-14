import pytest
from datetime import datetime

from setup import *

# set DATEFORMAT YMD
""" Тут только положительные тесты.
Любой обвал теста - причина для создания таски.
Перед стартом нужно снести все старые тестовые данные, чтобы не было разночтений.
В тестах не учитываем незавершенные осмотры. Они на ОБД не идут."""


def test_transfer_of_exams():
    """ Проверяем прохождение измерений между ТПР и сервер
    ТПР 11.10.10.51, Сервер 11.10.10.1
    Проект МГОК.
    Делаем допуск + 1 измерение, для возможных таймаутов в передаче.
    Запрос делается на день момента запуска теста, т.е. тестовые данные должны уже быть"""
    server, tpr = server_return(), tpr_return()
    assert tpr == server or tpr == (server + 1)


# @pytest.mark.skip
def test_serv_obd():
    """Проверяем проход данных с сервера на ТПР.
    Условия и каунты те же, с небольшим изменение по типу. Смотреть setup
    База ОБД живет на 11.10.10.1
    Даем больший допуск по отставанию каунта измерений. Максимально что можем допустить это 5"""
    result = approximately_equal()
    assert True is result


def test_count():
    """Даем каунт
    сервер - тпр
    сервер - обд где ExamResultID != 5"""
    server, tpr, obd, serv_obd = server_return(), tpr_return(), obd_return(), server_obd_return()
    print('\nCount:')
    print('Общее: Сервер {0} ТПР {1}'.format(server, tpr))
    print('Валидное: Сервер {0} ОБД {1}'.format(serv_obd, obd))


@pytest.fixture(autouse=True)
def time_delta():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    print(f'\nВремя на тест: {end_time - start_time}')
