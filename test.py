import unittest
from main import add

class TestAddFunction(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        self.assertEqual(add(5, 7), 12)
        
    def test_add_negative_numbers(self):
        self.assertEqual(add(-3, -4), -7)
        
    def test_add_mixed_numbers(self):
        self.assertEqual(add(-5, 10), 5)
        
    def test_add_zero(self):
        self.assertEqual(add(8, 0), 8)
        self.assertEqual(add(0, 0), 0)
        
if __name__ == "__main__":
    unittest.main()