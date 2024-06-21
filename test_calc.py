import unittest
from calc import Calc

class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-3, 5), 2)
        self.assertEqual(self.calc.add(3, -5), -2)

    def test_sub(self):
        self.assertEqual(self.calc.sub(2, 3), -1)

    def test_mul(self):
        self.assertEqual(self.calc.mul(2, 3), 6)

    #my tests
    def test_div(self):
      self.assertEqual(self.calc.div(4, 4), 1)
      with self.assertRaises(ZeroDivisionError):
        self.calc.div(3, 0)
    
    def test_pow(self):
      self.assertEqual(self.calc.pow(2, 2), 4)
      self.assertEqual(self.calc.pow(2, 0), 1)

    def test_sqrt(self):
      self.assertEqual(self.calc.sqrt(36), 6)
      self.assertEqual(self.calc.sqrt(20), 4.47213595499958)

