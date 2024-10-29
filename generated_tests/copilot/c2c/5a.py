import unittest
from c2c import intersperse

class TestIntersperse(unittest.TestCase):
    
    def test_intersperse_with_positive_numbers(self):
        self.assertEqual(intersperse([1, 2, 3], 0), [1, 0, 2, 0, 3])
    
    def test_intersperse_with_negative_numbers(self):
        self.assertEqual(intersperse([-1, -2, -3], 0), [-1, 0, -2, 0, -3])
    
    def test_intersperse_with_mixed_numbers(self):
        self.assertEqual(intersperse([1, -2, 3], 0), [1, 0, -2, 0, 3])
    
    def test_intersperse_with_single_number(self):
        self.assertEqual(intersperse([1], 0), [1])
    
    def test_intersperse_with_empty_list(self):
        self.assertEqual(intersperse([], 0), [])

if __name__ == '__main__':
    unittest.main()