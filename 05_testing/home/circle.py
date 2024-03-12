from math import pi

class Ex_Example(Exception):
    pass

class Circle:
    def __init__(self, radius: int):
        # try:
        #     if radius > 0:
        #         self._radius = radius
        #     else:
        #         raise Ex_Example
        # except Ex_Example:
        #     print('it is imposible, radius become ZERO')
        #     self._radius = 0

        self._radius = radius

        # if radius>0:
        #
        # else:
        #     raise Ex_Example('it is imposible, radius become ZERO')



    def get_len(self):
        return 2 * pi * self._radius

    def get_area(self):
        return pi * self._radius ** 2

    def __str__(self):
        if self._radius>0:
            return f'Длина окружности = {self.get_len():.3f} \n Площадь окружности = {self.get_area():.3f}'
        else:
            return f'Круг не создан, поэтому: \n   Длина окружности = {self.get_len():.3f} \n   Площадь окружности = {self.get_area():.3f}'


circle = Circle(5)
circle1 = Circle(-7)

print(circle)
print(circle1)


