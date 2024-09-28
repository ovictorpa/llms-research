import unittest
from typing import List
from your_module_name import rescale_to_unit  # Replace 'your_module_name' with the actual module name

class TestRescaleToUnit(unittest.TestCase):

    def test_normal_case(self):
        input_list = [1.0, 2.0, 3.0, 4.0, 5.0]
        expected_output = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(rescale_to_unit(input_list), expected_output)

    def test_single_element(self):
        input_list = [42.0]
        expected_output = [0.0]
        self.assertEqual(rescale_to_unit(input_list), expected_output)

    def test_all_same_values(self):
        input_list = [10.0, 10.0, 10.0]
        expected_output = [0.0, 0.0, 0.0]
        self.assertEqual(rescale_to_unit(input_list), expected_output)

    def test_negative_values(self):
        input_list = [-5.0, -2.0, 0.0, 3.0, 8.0]
        expected_output = [0.0, 0.23076923076923078, 0.38461538461538464, 0.6153846153846154, 1.0]
        self.assertAlmostEqual(rescale_to_unit(input_list), expected_output)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            rescale_to_unit([])

    def test_input_type(self):
        with self.assertRaises(TypeError):
            rescale_to_unit([1, 2, 3])  # Integer list instead of float

if __name__ == '__main__':
    unittest.main()
