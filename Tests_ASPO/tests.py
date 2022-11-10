from setup import *

""" Тут только положительные тесты.
Любой обвал теста - причина для создания таски"""
def test_transfer_of_exams():
    """ Проверяем прохождение измерений между ТПР и сервер
    ТПР 11.10.10.51, Сервер 11.10.10.1
    Проект МГОК
    Делаем допуск + 1 измерение, для возможных таймаутов в передаче
    Запрос делаеться на день момента запуска теста, т.е. тестовые данные должны уже быть"""
    server = server_return()
    tpr = tpr_return()
    assert tpr == server or tpr == (server+1)
