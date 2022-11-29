import pytest


def python_string_slicer(x):
    if x > 0:
        z = x ** 2
        return z
    else:
        return 1


@pytest.fixture(scope="function", params=[10, 11, 12, 13, 14, 0])
def param_fun(request):
    return request.param


def test_python_string_slicer(param_fun):
    result = python_string_slicer(param_fun)
    print(result)
    assert result != 100

