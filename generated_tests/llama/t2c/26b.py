import unittest
from collections import Counter

class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates_single_element(self):
        numbers = [1, 1]
        expected_result = []
        self.assertEqual(remove_duplicates(numbers), expected_result)

    def test_remove_duplicates_two_elements(self):
        numbers = [1, 2, 2, 3, 4, 4, 5]
        expected_result = [1, 2, 3, 4, 5]
        self.assertEqual(remove_duplicates(numbers), expected_result)

    def test_remove_duplicates_three_elements(self):
        numbers = [1, 2, 2, 3, 3, 3]
        expected_result = []
        self.assertEqual(remove_duplicates(numbers), expected_result)

    def test_remove_duplicates_order_preserved(self):
        numbers = [4, 5, 5, 6, 7, 8, 9]
        expected_result = [4, 5, 6, 7, 8, 9]
        self.assertEqual(remove_duplicates(numbers), expected_result)

    def test_remove_duplicates_empty_list(self):
        numbers = []
        expected_result = []
        self.assertEqual(remove_duplicates(numbers), expected_result)

if __name__ == '__main__':
    unittest.main()