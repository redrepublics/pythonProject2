# import pytest
# from datetime import datetime
#
#
# def python_string_slicer(x):
#     if x > 0:
#         z = x ** 2
#         return z
#     else:
#         return 1
#
#
# @pytest.fixture(scope="function", params=[10, 11, 12, 13, 14, 0, 'str'])
# def param_fun(request):
#     return request.param
#
#
# def test_python_string_slicer(param_fun):
#     result = python_string_slicer(param_fun)
#     print('\nТест для входного параметра {0}'.format(result), type(result))
#     assert result < 150
#
#
# @pytest.fixture(autouse=True)
# def time_delta():
#     start_time = datetime.now()
#     yield
#     end_time = datetime.now()
#     print(f'\nВремя на тест: {end_time - start_time}')


# def sum_test(x, y):
#     try:
#         result = int(x) + int(y)
#     except ValueError and UnboundLocalError as file:
#         print('Плохое число через Enter')
#     print('Сложение: {0} + {1} = {2}'.format(x, y, result))
#
#
# def self_tt():
#     print('Введите два целых числа')
#     sum_test(input(), input())
#
#
#
# self_tt()
#
# x = 1_000_000
# print(f'{x:,}')
a = [1, 2, 3, 2]
b = {1, 2, 3, 3}
print(sorted(a) == sorted(b))
