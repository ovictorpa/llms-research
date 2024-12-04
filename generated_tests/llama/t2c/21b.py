import unittest
from your_module import rescale_to_unit 

class TestRescaleToUnit(unittest.TestCase):

    def test_rescale_to_unit_single_element(self):
        self.assertEqual(rescale_to_unit([1.0]), [0.0])

    def test_rescale_to_unit_no_elements(self):
        with self.assertRaises(ValueError):
            rescale_to_unit([])

    def test_rescale_to_unit_equal_numbers(self):
        self.assertEqual(rescale_to_unit([1.0, 1.0, 1.0, 1.0]), [0.0, 0.0, 0.0, 0.0])

    def test_rescale_to_unit_all_zeros(self):
        self.assertEqual(rescale_to_unit([0.0, 0.0, 0.0, 0.0]), [0.0, 0.0, 0.0, 0.0])

    def test_rescale_to_unit_all_ones(self):
        self.assertEqual(rescale_to_unit([1.0, 1.0, 1.0, 1.0]), [0.0, 0.25, 0.5, 0.75])

    def test_rescale_to_unit_random_numbers(self):
        numbers = [10.0, -2.0, 3.0, 7.0]
        expected_result = [-1.0, -0.6666666666666666, 0.0, 0.3333333333333333]
        self.assertEqual(rescale_to_unit(numbers), expected_result)

if __name__ == '__main__':
    unittest.main()