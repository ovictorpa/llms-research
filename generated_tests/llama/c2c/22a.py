import unittest

class TestFilterIntegersFunction(unittest.TestCase):

    def test_empty_list(self):
        # Test with an empty list
        self.assertEqual(filter_integers([]), [])

    def test_single_integer(self):
        # Test with a single integer in the list
        self.assertEqual(filter_integers([5]), [5])

    def test_multiple_integers(self):
        # Test with multiple integers in the list
        self.assertEqual(filter_integers([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_non_integer_elements(self):
        # Test with non-integer elements in the list
        self.assertEqual(filter_integers(['a', 'b', 3, 4.5, None]), [3])

    def test_mixed_list(self):
        # Test with a mixed list of integers and non-integers
        self.assertEqual(filter_integers([1, 'a', 3, 4.5, None, 6]), [1, 3, 6])

    def test_large_input(self):
        # Test with a large input
        values = [i for i in range(1, 100)]
        result = filter_integers(values)
        expected_result = list(range(1, 100))
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()