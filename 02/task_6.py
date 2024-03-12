"""
Задание №6
📌 Доработайте прошлую задачу.
📌 Добавьте сравнение прямоугольников по площади
📌 Должны работать все шесть операций сравнения
"""


class Rectangle:

    def __init__(self, side_a, side_b=0):
        self.side_a = side_a
        if side_b == 0:
            side_b = side_a
        self.side_b = side_b

    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)

    def get_area(self):
        return self.side_a * self.side_b

    def __add__(self, other):
        new_per = self.get_perimeter() + other.get_perimeter()
        return Rectangle(new_per / 2 - self.side_b, self.side_b)  # делаем прямоугольник со стороной Б

    def __sub__(self, other):
        new_per = abs(self.get_perimeter() - other.get_perimeter())
        return Rectangle(new_per / 2 - self.side_b / 2, self.side_b / 2)  # делаем прямоугольник со стороной Б/2

    def __eq__(self, other):  # равно ==
        return self.get_area() == other.area()

    def __ne__(self, other):  # неравно !=
        return self.get_area() != other.area()

    def __gt__(self, other):  # больше >
        return self.get_area() > other.area()

    def __ge__(self, other):  # больше или равно >=
        return self.get_area() >= other.area()

    def __lt__(self, other):  # метод меньше <
        return self.get_area() < other.area()

    def __le__(self, other):  # меньше или равно <=
        return self.get_area() <= other.area()

    def __str__(self):
        result = f'Square= {self.get_area():.2f} side A= {self.side_a:.2f} side B= {self.side_b}'
        return result


rectangle1 = Rectangle(7.3)
print(rectangle1)
rectangle2 = Rectangle(5.6, 10.2)
print(rectangle2)
ren = rectangle1+rectangle2
print(ren)

# print(f'площадь 1 прямоугольника = {rectangle1.get_area():.2f}')
# print(f'площадь 2 прямоугольника = {rectangle2.get_area():.2f}')
# print(rectangle1 == rectangle2)
print(f'({rectangle1.get_area():.2f} = {rectangle2.get_area():.2f}):',
      rectangle1 == rectangle2)
print(f'({rectangle1.get_area():.2f} != {rectangle2.get_area():.2f}):',
      rectangle1 != rectangle2)
print(f'({rectangle1.get_area():.2f} > {rectangle2.get_area():.2f}):',
      rectangle1 > rectangle2)
print(f'({rectangle1.get_area():.2f} <= {rectangle2.get_area():.2f}):',
      rectangle1 <= rectangle2)
print(f'({rectangle1.get_area():.2f} < {rectangle2.get_area():.2f}):',
      rectangle1 < rectangle2)
print(f'({rectangle1.get_area():.2f} >= {rectangle2.get_area():.2f}):',
      rectangle1 >= rectangle2)
