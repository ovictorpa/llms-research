import unittest

class TestSumProductFunction(unittest.TestCase):

    def test_empty_list(self):
        # Test with an empty list
        self.assertEqual(sum_product([]), (0, 1))

    def test_single_element_list(self):
        # Test with a single element list
        self.assertEqual(sum_product([5]), (5, 5))

    def test_multiple_elements_list(self):
        # Test with multiple elements list
        self.assertEqual(sum_product([1, 2, 3, 4, 5]), (15, 120))

    def test_non_integer_element(self):
        # Test with a non-integer element in the list
        with self.assertRaises(TypeError):
            sum_product([1, 'a', 3])

    def test_non_list_input(self):
        # Test that type error is raised when input is not a list
        with self.assertRaises(TypeError):
            sum_product(123)

    def test_large_input(self):
        # Test with a large input
        result = sum_product([1, 2, 3, 4, 5])
        expected_sum = 15
        expected_prod = 120
        self.assertEqual(result, (expected_sum, expected_prod))

if __name__ == '__main__':
    unittest.main()