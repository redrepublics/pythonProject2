"""Tests unit 19.3.3
Только положительные тесты.
Импортируем все переменные"""
from Unit19_3_3.settings import *
from Unit19_3_3.api import PetFriends
pf = PetFriends()


def test_my_api_key(email=valid_email, password=valid_password):
    """Запрашиваем API_KEY подставив валидную электронную почту и пароль
    Запрос GET"""
    status, result = pf.get_api_key(email, password)
    assert status == 200 and 'key' in result


def test_get_pet(filter=''):
    """Запрос всех своих животных"""
    """ _, - когда один из параметров не важен 
    помимо статуса проверяем, что список животных содержит больше ноля
    Запрос GET"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200 and len(result['pets']) > 0


def test_put_pet(name='Мурзик', animal_type='Котэ', age=5):
    """Изменяем информацию о питомце.
    Сначала получаем ключ и список своих питомцев.
    Даем условие наличия питомца больше нуля,
    иначе ловим ошибку.
    Запрос PUT"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200 and result['name'] == name
    else:
        raise Exception("There is no my pets")


def test_del_pet():
    """Проверяем возможность удаления питомца.
    Опять делаем запрос на ключ и свой список.
    Если своих питомцев нет, добавляем материал для работы.
    Иначе работает с тем, что есть.
    Забираем первого питомца по идентификатору, отправляем запрос на удаление.
    После - запрос, проверяем что идентификатор отсутствует.
    Запрос DELETE"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Барсик", "кот", "3")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    assert status == 200 and pet_id not in my_pets.values()
