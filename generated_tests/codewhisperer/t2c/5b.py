import unittest
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of the input list `numbers`.
    
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    # Function implementation goes here
    # For testing purposes, we'll assume the function is correctly implemented

class TestIntersperse(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_example_case(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_single_element(self):
        self.assertEqual(intersperse([5], 0), [5])

    def test_two_elements(self):
        self.assertEqual(intersperse([1, 2], 3), [1, 3, 2])

    def test_negative_numbers(self):
        self.assertEqual(intersperse([-1, -2, -3], -4), [-1, -4, -2, -4, -3])

    def test_mixed_positive_negative(self):
        self.assertEqual(intersperse([-1, 0, 1], 2), [-1, 2, 0, 2, 1])

    def test_zero_delimiter(self):
        self.assertEqual(intersperse([1, 2, 3], 0), [1, 0, 2, 0, 3])

    def test_large_numbers(self):
        self.assertEqual(intersperse([1000000, 2000000], 3000000), [1000000, 3000000, 2000000])

    def test_delimiter_in_list(self):
        self.assertEqual(intersperse([1, 2, 3, 4], 2), [1, 2, 2, 2, 3, 2, 4])

    def test_non_int_input(self):
        with self.assertRaises(TypeError):
            intersperse([1.0, 2.0], 3)

    def test_non_int_delimiter(self):
        with self.assertRaises(TypeError):
            intersperse([1, 2], 3.0)

if __name__ == '__main__':
    unittest.main()
