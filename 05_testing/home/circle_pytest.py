import pytest

from circle import Circle


def test_1():
    assert Circle(-5) == 'it is imposible, radius become ZERO', 'ошибка тест 1'

if __name__ == '__main__':
    pytest.main(['-v'])