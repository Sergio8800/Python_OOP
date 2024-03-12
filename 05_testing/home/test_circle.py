# from circle import Circle
import doctest

from math import pi


class Ex_Example(Exception):
    pass


class Circle:
    """
    >>> Circle(-5)
    it is imposible, radius become ZERO
    """

    def __init__(self, radius: int):
        try:
            if radius > 0:
                self._radius = radius
            else:
                raise Ex_Example
        except Ex_Example:
            print('it is imposible, radius become ZERO')
            self._radius = 0
        # if radius>0:
        #     self._radius = radius
        # else:
        #     raise Ex_Example

    def get_len(self):
        return 2 * pi * self._radius

    def get_area(self):
        return pi * self._radius ** 2

    def __str__(self):
        return f'Длина окружности = {self.get_len():.3f} \n Площадь окружности = {self.get_area():.3f}'


# def test_circle():
#     """
#     >>> Circle(-5)
#     it is imposible, radius will be 1
#     """


if __name__ == '__main__':
    # c = Circle(-5)
    doctest.testmod(verbose=True)
