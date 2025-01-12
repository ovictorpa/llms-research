import unittest
from typing import List, Any
from c2c.22a import filter_integers  # Adjust the import statement as needed

class TestFilterIntegers(unittest.TestCase):

    def test_mixed_types(self):
        input_list = [1, 'a', 3.14, 2, True, 5, '10', [1, 2], 8]
        expected_output = [1, 2, 5, 8]
        self.assertEqual(filter_integers(input_list), expected_output)

    def test_all_integers(self):
        input_list = [1, 2, 3, 4, 5]
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(filter_integers(input_list), expected_output)

    def test_no_integers(self):
        input_list = ['a', 3.14, True, '10', [1, 2]]
        expected_output = []
        self.assertEqual(filter_integers(input_list), expected_output)

    def test_empty_list(self):
        input_list = []
        expected_output = []
        self.assertEqual(filter_integers(input_list), expected_output)

    def test_negative_integers(self):
        input_list = [-1, 2, -3, 4.5, '-5', -6]
        expected_output = [-1, 2, -3, -6]
        self.assertEqual(filter_integers(input_list), expected_output)

    def test_large_integers(self):
        input_list = [10**9, 10**10, 10**11, 10.5, '1000000000']
        expected_output = [10**9, 10**10, 10**11]
        self.assertEqual(filter_integers(input_list), expected_output)

if __name__ == '__main__':
    unittest.main()
