import unittest
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    # Function implementation goes here
    # For testing purposes, we'll leave this empty
    pass

class TestFilterIntegers(unittest.TestCase):
    def test_example_case_1(self):
        input_list = ['a', 3.14, 5]
        expected_output = [5]
        self.assertEqual(filter_integers(input_list), expected_output)

    def test_example_case_2(self):
        input_list = [1, 2, 3, 'abc', {}, []]
        expected_output = [1, 2, 3]
        self.assertEqual(filter_integers(input_list), expected_output)

    def test_empty_list(self):
        input_list = []
        expected_output = []
        self.assertEqual(filter_integers(input_list), expected_output)

    def test_no_integers(self):
        input_list = ['a', 'b', 3.14, [], {}, True, False]
        expected_output = []
        self.assertEqual(filter_integers(input_list), expected_output)

    def test_only_integers(self):
        input_list = [1, 2, 3, 4, 5]
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(filter_integers(input_list), expected_output)

    def test_negative_integers(self):
        input_list = [-1, 0, 1, -2, 2]
        expected_output = [-1, 0, 1, -2, 2]
        self.assertEqual(filter_integers(input_list), expected_output)

    def test_large_integers(self):
        input_list = [10**9, 10**10, 10**11]
        expected_output = [10**9, 10**10, 10**11]
        self.assertEqual(filter_integers(input_list), expected_output)

    def test_mixed_types(self):
        input_list = [1, 'two', 3.0, [4], {'five': 5}, 6, True, 7.5, -8]
        expected_output = [1, 6, -8]
        self.assertEqual(filter_integers(input_list), expected_output)

    def test_boolean_not_included(self):
        input_list = [True, False, 1, 0]
        expected_output = [1, 0]
        self.assertEqual(filter_integers(input_list), expected_output)

    def test_input_unchanged(self):
        input_lis        original_input = input_list.copy()
        filter_integers(input_list)
        self.assertEqual(input_list, original_input, "Input list should not be modified")

if __name__ == '__main__':
    unittest.main()
