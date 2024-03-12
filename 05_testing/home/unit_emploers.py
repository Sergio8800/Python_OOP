import unittest

class Person:

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

class Employee(Person):

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, position: str, salary: float):
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = salary

    def raise_salary(self, percent: float):
        self.salary *= (1 + percent / 100)

    def __str__(self):
        return f'{self.full_name()} ({self.position})'


class TestCaseName(unittest.TestCase):
    """Тестирование функции """

    def setUp(self):
        self.person = Employee("Ivanov", "Ivan", "Ivanovich", 30,"manager",50000)
    def test_employee_full_name(self):
        self.assertEqual(self.person.full_name(), "Ivanov Ivan Ivanovich")
    def test_employee_birthday(self):
        self.person.birthday()
        self.assertEqual(self.person.get_age(), 31)
    def test_employee_raise_salary(self):
        self.person.raise_salary(10)
        self.assertEqual(self.person.salary,  55000.00000000001)

    def test_employee_str(self):
        self.assertEqual(self.person.__str__(), "Ivanov Ivan Ivanovich (Manager)")

    def test_employee_last_name_title(self):
        self.person = Employee("ivanov", "Ivan", "Ivanovich", 30, "manager", 50000)
        self.assertEqual(self.person.last_name, "Ivanov")



if __name__ == '__main__':
    unittest.main(verbosity=2)
