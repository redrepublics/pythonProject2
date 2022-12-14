from Unit19_4.api import PetFriends
from Unit19_4.settings import *
import os


pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в тезультате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
    запрашиваем список всех питомцев и проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_with_valid_data(name='Барбоскин', animal_type='двортерьер', age='4', pet_photo='images/cat1.jpg'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # Если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


"""req 19.7.2"""


# req 1
def test_no_valid_email(email=no_valid_email, password=valid_password):
    """ Проверяем что запрос api не проходит при некорректных учетных данных - почта"""
    status, result = pf.get_api_key(email, password)
    assert status != 200 and 'found in database' in result


# req 2
def test_no_valid_password(email=valid_email, password=no_valid_password):
    """ Проверяем что запрос api не проходит при некорректных учетных данных - неправильный пароль"""
    status, result = pf.get_api_key(email, password)
    assert status != 200 and 'found in database' in result


# req 3
def test_get_list_of_pets_with_wrong_no_auth_key(filter='my_pets'):
    """ Проверяем что запрос списка питомцев с неверным auth_key выдаёт ошибку.
    Изменяем полученный key"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key['key'] += str(generate_random_string(10))
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 403 or status != 200


# req 4
def test_successful_delete_self_no_pet():
    """Проверяем то что не может удалить того, чего нет.
    Для этого портим идентификатор питомца генерируя добавочное значение.
    Для этого берем реальный ID. Результат подобного запроса должен быть пуст.
    """
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    pet_id += str(generate_random_string(10))
    status, result = pf.delete_pet(auth_key, pet_id)
    assert result == ''


# req 5
def test_no_pet():
    """ Проверяем что не может вывести информацию подставив фиктивный ID
    Для этого ищем своего питомца в списке, по рандомному ID в 1000 знаков"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    id_no = str(generate_random_string(1000))
    status, _ = pf.get_list_of_pets(auth_key, id_no)
    assert status == 500


# req 6
def test_add_new_pet_with_no_valid_photo(name='Плохое имя', animal_type='плохой тип', age='4', pet_photo='images/cat1.txt'):
    """Проверяем что нельзя добавить неправильный формат в фото, скажем вместо jpg дать txt.
    Запрос должен пройти с пустым параметром pet_photo.
    Указываем неправильный формат, получаем ключ, добавляем, сверяем результат."""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert 'data:image/jpeg' not in result
