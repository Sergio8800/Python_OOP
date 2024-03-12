from regt_unit import Rectangle
import pytest


@pytest.fixture
def func():
    obj = Rectangle(4, 5)
    return obj

@pytest.fixture
def func2():
    obj = Rectangle(3, 4)
    return obj

def test_width(func):
    assert func.width ==4

def test_height(func2):
    assert func2.height ==4

def test_perimetr(func):
    assert func.perimeter() == 18


def test_aria(func):
    assert func.area() == 20


if __name__ == '__main__':
    pytest.main(['-v'])
