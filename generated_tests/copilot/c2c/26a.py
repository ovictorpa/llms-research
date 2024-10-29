import unittest
from c2c import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates_with_no_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_remove_duplicates_with_all_duplicates(self):
        self.assertEqual(remove_duplicates([1, 1, 2, 2, 3, 3]), [])

    def test_remove_duplicates_with_some_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 4, 4, 5]), [1, 3, 5])

    def test_remove_duplicates_with_single_element(self):
        self.assertEqual(remove_duplicates([1]), [1])

    def test_remove_duplicates_with_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_remove_duplicates_with_negative_numbers(self):
        self.assertEqual(remove_duplicates([-1, -2, -2, -3, -4, -4, -5]), [-1, -3, -5])

    def test_remove_duplicates_with_mixed_numbers(self):
        self.assertEqual(remove_duplicates([1, -1, 2, -2, 2, -2, 3, -3]), [1, -1, 3, -3])

if __name__ == '__main__':
    unittest.main()