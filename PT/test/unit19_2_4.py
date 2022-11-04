import pytest
from app.calculator import Calculator


# Ссылку на репозиторий опубликуйте в задании unit 19.7.3

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_multiply_success(self):
        assert self.calc.multiply(self, 2, 5) == 10

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 10, 5) == 5

    def test_division_success(self):
        assert self.calc.division(self, 10, 5) == 2

    def test_adding_failure(self):
        assert self.calc.adding(self, 1, 1) == 3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def teardown(self):
        print('Используем метод Teardown')
