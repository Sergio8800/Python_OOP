import unittest

from circle import Circle


class TestCaseName(unittest.TestCase):
    """Тестирование функции convert_str"""

    def test_method_1(self):
        self.assertEqual(Circle(-5), 'it is imposible, radius become ZERO')



if __name__ == '__main__':
    unittest.main(verbosity=2)