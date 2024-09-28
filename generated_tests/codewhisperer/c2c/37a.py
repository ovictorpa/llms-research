import unittest
from typing import List
from c2c.37a import sort_even  # Adjust the import statement as needed

class TestSortEven(unittest.TestCase):

    def test_basic_case(self):
        input_list = [5, 3, 2, 8, 1, 9, 0, 7]
        expected_output = [0, 3, 2, 8, 5, 9, 1, 7]
        self.assertEqual(sort_even(input_list), expected_output)

    def test_already_sorted(self):
        input_list = [1, 2, 3, 4, 5, 6]
        expected_output = [1, 2, 3, 4, 5, 6]
        self.assertEqual(sort_even(input_list), expected_output)

    def test_reverse_sorted(self):
        input_list = [6, 5, 4, 3, 2, 1]
        expected_output = [2, 5, 4, 3, 6, 1]
        self.assertEqual(sort_even(input_list), expected_output)

    def test_odd_length_list(self):
        input_list = [5, 3, 2, 8, 1, 9, 0]
        expected_output = [0, 3, 2, 8, 5, 9, 1]
        self.assertEqual(sort_even(input_list), expected_output)

    def test_even_length_list(self):
        input_list = [5, 3, 2, 8, 1, 9]
        expected_output = [2, 3, 5, 8, 1, 9]
        self.assertEqual(sort_even(input_list), expected_output)

    def test_single_element(self):
        input_list = [42]
        expected_output = [42]
        self.assertEqual(sort_even(input_list), expected_output)

    def test_two_elements(self):
        input_list = [2, 1]
        expected_output = [2, 1]
        self.assertEqual(sort_even(input_list), expected_output)

    def test_empty_list(self):
        input_list: List[int] = []
        expected_output: List[int] = []
        self.assertEqual(sort_even(input_list), expected_output)

    def test_all_same_elements(self):
        input_list = [1, 1, 1, 1, 1]
        expected_output = [1, 1, 1, 1, 1]
        self.assertEqual(sort_even(input_list), expected_output)

    def test_negative_numbers(self):
        self.assertEqual(sort_even(input_list), expected_output)

if __name__ == '__main__':
    unittest.main()
