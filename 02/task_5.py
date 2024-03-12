"""
Задание №5
📌 Дорабатываем класс прямоугольник из прошлого семинара.
📌 Добавьте возможность сложения и вычитания.
📌 При этом должен создаваться новый экземпляр
прямоугольника.
📌 Складываем и вычитаем периметры, а не длинну и ширину.
📌 При вычитании не допускайте отрицательных значений.
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
        return Rectangle(new_per/2-self.side_b, self.side_b) # делаем прямоугольник со стороной Б

    def __sub__(self, other):
        new_per = abs(self.get_perimeter() - other.get_perimeter())
        return Rectangle(new_per/2-self.side_b/2, self.side_b/2) # делаем прямоугольник со стороной Б/2


rectangle1 = Rectangle(7.3)
rectangle2 = Rectangle(5.6, 10.2)
rectangle3 = rectangle1 + rectangle2
rectangle4 = rectangle3 - rectangle2

print(f'Периметр 1 прямоугольника = {rectangle1.get_perimeter():.2f}')
print(f'Периметр 2 прямоугольника = {rectangle2.get_perimeter():.2f}')

print(f'Периметр 3 прямоугольника = {rectangle3.get_perimeter():.2f}')
print(f'Периметр 4 прямоугольника = {rectangle4.get_perimeter():.2f}')
