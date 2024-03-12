import doctest


class Person:

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        """
        >>> person = Employee("Ivanov", "Ivan", "Ivanovich", 30,"3e",11)
        >>> person.full_name()
        'Ivanov Ivan Ivanovich'
        """
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
        """
        >>> person = Employee("Ivanov", "Ivan", "Ivanovich", 30,"manager",50000)
        >>> person.raise_salary(10)
        >>> person.salary
        55000.00000000001
        """
        self.salary *= (1 + percent / 100)

    def __str__(self):
        """
        >>> person = Employee("Ivanov", "Ivan", "Ivanovich", 30,"manager",50000)
        >>> print(person)
        Ivanov Ivan Ivanovich (Manager)
        """
        return f'{self.full_name()} ({self.position})'

if __name__ == '__main__':
    person = Employee("Ivanov", "Ivan", "Ivanovich", 30,"3e",11)
    print(person.full_name())
    print(person.birthday())
    doctest.testmod(verbose=True)  # чтобы увидеть рез-т