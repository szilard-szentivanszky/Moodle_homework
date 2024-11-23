import unittest
from calculator import Calculator

class TestCalculatorIntegration(unittest.TestCase):
    def test_add_integration(self):
        calc = Calculator()
        result = calc.add(2, 3)
        # Feltételezzük, hogy az eredményt valamilyen módon tovább feldolgozzuk
        self.assertTrue(isinstance(result, int))
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()

