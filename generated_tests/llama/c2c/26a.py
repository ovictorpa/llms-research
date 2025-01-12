import unittest

class TestRemoveDuplicatesFunction(unittest.TestCase):

    def test_no_duplicates(self):
        # Test with no duplicates
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_duplicates_present(self):
        # Test with duplicates present
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 3, 3]), [1, 2, 3])

    def test_empty_list(self):
        # Test with an empty list
        self.assertEqual(remove_duplicates([]), [])

    def test_single_element_list(self):
        # Test with a single element list
        self.assertEqual(remove_duplicates([5]), [5])

    def test_large_input(self):
        # Test with a large input
        numbers = list(range(1, 100))
        unique_numbers = remove_duplicates(numbers)
        self.assertEqual(len(unique_numbers), len(set(numbers)))

    def test_non_integer_element(self):
        # Test with non-integer element
        with self.assertRaises(TypeError):
            remove_duplicates([1, '2', 3])

if __name__ == '__main__':
    unittest.main()