import unittest
from your_module import sort_even  # Replace with the actual module name

class TestSortEven(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sort_even([]), [])

    def test_single_element_list(self):
        self.assertEqual(sort_even([1]), [1])

    def test_even_length_list(self):
        self.assertEqual(sort_even([2, 3, 4, 5]), [2, 3, 4, 5])

    def test_odd_length_list(self):
        self.assertEqual(sort_even([2, 3, 4, 5, 6]), [2, 3, 4, 5, 6])

    def test_multiple_rods(self):
        self.assertEqual(sort_even([1, 2, 3, 4, 5, 6, 7]), [1, 2, 3, 4, 5, 6, 7])

    def test_unordered_input(self):
        input_list = [6, 4, 8, 3, 1, 9, 7, 2, 5]
        expected_output = [1, 2, 3, 4, 5, 6, 8, 9]
        self.assertEqual(sort_even(input_list), expected_output)

if __name__ == '__main__':
    unittest.main()