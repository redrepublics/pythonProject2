#дальнейший разбор и применение
class Employee:
    """Базовый класс для всех сотрудников"""
    emp_count = 0
    global dict1, dict2, dict3
    dict1, dict2, dict3 = 'IT', 'Бухгалтерия', 'Охрана'


    def __init__(self, name, salary, dist, age):
        self.name = name
        self.salary = salary
        self.dist = dist
        self.age = age
        Employee.emp_count += 1

    def display_count(self):
        print('Всего сотрудников: %d' % Employee.emp_count)

    def display_employee(self):
        print('Имя: {}. Зарплата: {}. Отдел: {}. Возраст: {}.'.format(self.name, self.salary, self.dist, self.age))

    def is_age_emp(self):
        return True if self.age > 20 else False



emp1 = Employee("Андрей", 2000, dict1, 20)
emp2 = Employee("Мария", 5000, dict2, 35)
emp3 = Employee("Денис", 2000, dict3, 40)
emp1.display_employee()
emp2.display_employee()
emp3.display_employee()
emp1.is_age_emp()
emp2.is_age_emp()
emp3.is_age_emp()
print("Всего сотрудников: %d" % Employee.emp_count)
