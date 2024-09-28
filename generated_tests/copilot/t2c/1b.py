import unittest
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """

class TestHasCloseElements(unittest.TestCase):
    def test_no_close_elements(self):
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0], 0.5))

    def test_some_close_elements(self):
        self.assertTrue(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))

    def test_empty_list(self):
        self.assertFalse(has_close_elements([], 0.5))

    def test_single_element(self):
        self.assertFalse(has_close_elements([1.0], 0.5))

    def test_all_elements_same(self):
        self.assertTrue(has_close_elements([1.0, 1.0, 1.0], 0.1))

if __name__ == '__main__':
    unittest.main()