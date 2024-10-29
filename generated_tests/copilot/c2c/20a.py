import unittest
from c2c.a20 import find_closest_elements

class TestFindClosestElements(unittest.TestCase):
    
    def test_positive_numbers(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0]), (1.0, 2.0))
    
    def test_negative_numbers(self):
        self.assertEqual(find_closest_elements([-1.0, -2.0, -3.0, -4.0]), (-2.0, -1.0))
    
    def test_mixed_numbers(self):
        self.assertEqual(find_closest_elements([-1.0, 2.0, -3.0, 4.0]), (-1.0, 2.0))
    
    def test_single_element(self):
        self.assertEqual(find_closest_elements([1.0]), None)
    
    def test_empty_list(self):
        self.assertEqual(find_closest_elements([]), None)
    
    def test_identical_elements(self):
        self.assertEqual(find_closest_elements([1.0, 1.0, 1.0]), (1.0, 1.0))
    
    def test_large_numbers(self):
        self.assertEqual(find_closest_elements([1000.0, 2000.0, 3000.0, 4000.0]), (1000.0, 2000.0))

if __name__ == '__main__':
    unittest.main()