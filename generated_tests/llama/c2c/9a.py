import unittest
from your_module import rolling_max  # Replace with the actual module name

class TestRollingMax(unittest.TestCase):
    def test_empty_list(self):
        input_numbers = []
        expected_output = []
        self.assertEqual(rolling_max(input_numbers), expected_output)

    def test_single_element(self):
        input_numbers = [1]
        expected_output = [1]
        self.assertEqual(rolling_max(input_numbers), expected_output)

    def test_two_elements(self):
        input_numbers = [1, 2]
        expected_output = [1, 2]
        self.assertEqual(rolling_max(input_numbers), expected_output)

    def test_three_elements(self):
        input_numbers = [1, 2, 3]
        expected_output = [1, 2, 3]
        self.assertEqual(rolling_max(input_numbers), expected_output)

    def test_negative_numbers(self):
        input_numbers = [-1, -2, -3, -4]
        expected_output = [-1, -1, -1, -1]
        self.assertEqual(rolling_max(input_numbers), expected_output)

    def test_mixed_positive_and_negative(self):
        input_numbers = [1, 2, -3, 4, 5, -6]
        expected_output = [1, 2, 2, 4, 5, 5]
        self.assertEqual(rolling_max(input_numbers), expected_output)

if __name__ == '__main__':
    unittest.main()