"""Простой класс с атрибутами и методом"""


class Worker:
    """Класс-работник"""

    def __init__(self, name, surname, hours, rate):
        self.name = name
        self.surname = surname
        self._hours = hours
        self._rate = rate

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, val):
        if val < 0:
            raise ValueError(f'it will be positive {self._hours}')
        else:
            self._hours = val

    def total_profit(self):
        """Расчет зарплаты"""
        if self._hours < 0:
            raise ValueError(f'it will be positive {self._hours}')
# этот код необходим, на случай ввода данных при создании экземпляра класса, не проходит проверку через сетер...
        return self._hours * self._rate

    def __str__(self):
        return f'часы = {self._hours} ставка за час = {self._rate} ЗП = {self.total_profit()}'


OBJ = Worker('Иван', 'Иванов', 10, 100)
print(OBJ.total_profit())
print(OBJ)

OBJ.hours = 20
OBJ.rate = 200
print(OBJ)

# теперь попробуем присвоить какому-либо из атрибутов отрицательное значение

OBJ = Worker('Иван', 'Иванов', -10, 100)
print(OBJ.total_profit())
print(OBJ)

OBJ.hours = -10
OBJ.rate = 100
print(OBJ)

# проблема налицо(если не использовать @hours.setter) - значение атрибута при присвоении не проходит валидацию
# следовательно скрипт может отрабатывать некорректно, для rate не прописан @rate.setter
