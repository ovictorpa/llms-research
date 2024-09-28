import unittest
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Function implementation goes here
    # For testing purposes, we'll leave this empty
    pass

class TestRescaleToUnit(unittest.TestCase):
    def test_example_case(self):
        input_list = [1.0, 2.0, 3.0, 4.0, 5.0]
        expected_output = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(rescale_to_unit(input_list), expected_output)

    def test_negative_numbers(self):
        input_list = [-3.0, -1.0, 0.0, 2.0, 4.0]
        expected_output = [0.0, 0.2857142857142857, 0.42857142857142855, 0.7142857142857143, 1.0]
        self.assertAlmostEqual(rescale_to_unit(input_list), expected_output, places=7)

    def test_same_numbers(self):
        input_list = [5.0, 5.0, 5.0, 5.0]
        expected_output = [0.0, 0.0, 0.0, 0.0]
        self.assertEqual(rescale_to_unit(input_list), expected_output)

    def test_two_elements(self):
        input_list = [10.0, 20.0]
        expected_output = [0.0, 1.0]
        self.assertEqual(rescale_to_unit(input_list), expected_output)

    def test_large_numbers(self):
        input_list = [1000000.0, 2000000.0, 3000000.0]
        expected_output = [0.0, 0.5, 1.0]
        self.assertEqual(rescale_to_unit(input_list), expected_output)

    def test_small_numbers(self):
        input_list = [0.001, 0.002, 0.003, 0.004]
        expected_output = [0.0, 0.3333333333333333, 0.6666666666666666, 1.0]
        self.assertAlmostEqual(rescale_to_unit(input_list), expected_output, places=7)

    def test_input_unchanged(self):
        input_list = [1.0, 3.0, 5.0]
        original_input = input_list.copy()
        rescale_to_unit(input_list)
        self.assertEqual(input_list, original_input, "Input list should not be modified")

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            rescale_to_unit([])

    def test_single_element_list(self):
        with self.assertRaises(ValueError):
            rescale_to_unit([42.0])

if __name__ == '__main__':
    unittest.main()
