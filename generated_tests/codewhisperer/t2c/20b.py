import unittest
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two), select and return the two numbers that are closest to each other.
    The two numbers are returned in order (smaller number, larger number).
    
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Function implementation goes here
    # For testing purposes, we'll assume the function is correctly implemented

class TestFindClosestElements(unittest.TestCase):
    def test_example_cases(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0))

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            find_closest_elements([])

    def test_single_element_list(self):
        with self.assertRaises(ValueError):
            find_closest_elements([1.0])

    def test_all_elements_equal(self):
        self.assertEqual(find_closest_elements([1.0, 1.0, 1.0]), (1.0, 1.0))

    def test_negative_numbers(self):
        self.assertEqual(find_closest_elements([-1.0, -2.0, -3.0, -4.0, -5.0, -2.2]), (-2.2, -2.0))

    def test_mixed_positive_negative(self):
        self.assertEqual(find_closest_elements([-1.0, 2.0, -3.0, 4.0, -5.0, 2.2]), (2.0, 2.2))

    def test_large_list(self):
        numbers = [float(i) for i in range(1000000)]
        self.assertEqual(find_closest_elements(numbers), (0.0, 1.0))

    def test_non_float_input(self):
        with self.assertRaises(TypeError):
            find_closest_elements([1, 2.0, 3.0])

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            find_closest_elements(['a', 2.0, 3.0])

if __name__ == '__main__':
    unittest.main()
