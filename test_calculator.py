import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # Test cases for add()
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(3, 4), 7)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -5), -7)

    # Test cases for subtract()
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-3, -2), -1)

    # Test cases for multiply()
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(3, 5), 15)

    def test_multiply_negative_and_positive(self):
        self.assertEqual(self.calc.multiply(-4, 6), -24)

    # Test cases for divide()
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

    # Test cases for modulo()
    def test_modulo_positive_numbers(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.modulo(10, 0)

if __name__ == '__main__':
    unittest.main()
c