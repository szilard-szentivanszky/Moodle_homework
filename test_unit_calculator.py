import unittest
from calculator import Calculator

class TestCalculatorUnit(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()

