import unittest
from c2c._37a import sort_even

class TestSortEven(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sort_even([4, 3, 2, 1]), [2, 3, 4, 1])

    def test_negative_numbers(self):
        self.assertEqual(sort_even([-4, -3, -2, -1]), [-4, -3, -2, -1])

    def test_mixed_numbers(self):
        self.assertEqual(sort_even([4, -3, -2, 1]), [-2, -3, 4, 1])

    def test_single_number(self):
        self.assertEqual(sort_even([1]), [1])

    def test_empty_list(self):
        self.assertEqual(sort_even([]), [])

    def test_even_length(self):
        self.assertEqual(sort_even([10, 9, 8, 7, 6, 5]), [6, 9, 8, 7, 10, 5])

    def test_odd_length(self):
        self.assertEqual(sort_even([10, 9, 8, 7, 6]), [6, 9, 8, 7, 10])

if __name__ == '__main__':
    unittest.main()