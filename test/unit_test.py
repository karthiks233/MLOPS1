import unittest
from src import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(5, 0), 5)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-1, -1), -2)
        
    def test_sub(self):
        self.assertEqual(calculator.sub(2, 3), -1)
        self.assertEqual(calculator.sub(5, 0), 5)
        self.assertEqual(calculator.sub(-1, 1), -2)
        self.assertEqual(calculator.sub(-1, -1), 0)
        
    def test_mul(self):
        self.assertEqual(calculator.mul(2, 3), 6)
        self.assertEqual(calculator.mul(5, 0), 0)
        self.assertEqual(calculator.mul(-1, 1), -1)    
        
    def test_div(self):
        self.assertEqual(calculator.div(2, 1), 2)
        self.assertEqual(calculator.div(5, 2), 2.5)
        self.assertEqual(calculator.div(-1, -1), 1)
        self.assertEqual(calculator.div(-1, 100), -0.01)
        
if __name__ == "__main__":
    unittest.main()
    