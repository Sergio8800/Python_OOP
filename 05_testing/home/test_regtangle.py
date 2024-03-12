from regtangle_exept import Rectangle, NegativeValueError, Validator
import doctest


def test_width():
    """
    >>> reg = Rectangle(-5, 5)
    >>> print(reg)
    "__main__.NegativeValueError: Ширина должна быть положительной, а не -2"
    """

    # r1 = Rectangle(5, 5)
    # r1.perimeter()



if __name__ == '__main__':
    # r2 = Rectangle(-5, 5)
    # print(r2)
    doctest.testmod(verbose=True)
