import unittest
from your_module import find_closest_elements  # Replace 'your_module' with the actual name of the module where

class TestFindClosestElements(unittest.TestCase):

    def test_find_closest_elements_single_pair(self):
        self.assertEqual(find_closest_elements([1.0, 2.0]), (1.0, 2.0))

    def test_find_closest_elements_no_pairs(self):
        with self.assertRaises(ValueError):
            find_closest_elements([1.0])

    def test_find_closest_elements_multiple_pairs(self):
        self.assertEqual(find_closest_elements([-10.0, -5.0, 0.0, 2.0, 6.0]), (-5.0, 0.0))

    def test_find_closest_elements_unordered(self):
        self.assertEqual(find_closest_elements([1.0, 3.0, 2.0, 4.0]), (2.0, 3.0))

    def test_find_closest_elements_identical(self):
        self.assertEqual(find_closest_elements([1.0, 1.0]), (1.0, 1.0))
    