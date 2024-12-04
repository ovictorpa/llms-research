import unittest
from your_module import rescale_to_unit  # Replace with the actual module name

class TestRescaleToUnit(unittest.TestCase):
    def test_single_element(self):
        self.assertAlmostEqual(rescale_to_unit([1]), [0.0])

    def test_identical_elements(self):
        self.assertEqual(rescale_to_unit([-1, -1]), [-1.0] * 2)

    def test_min_max_same(self):
        self.assertEqual(rescale_to_unit([-10, -10]), [0.0] * 2)

    def test_min_max_diff(self):
        numbers = [-3, -2, -1, 0, 1, 2, 3]
        expected_result = [-1.0, -.5, 0, .5, 1.0, 1.5, 2.0]
        self.assertAlmostEqual(rescale_to_unit(numbers), expected_result)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            rescale_to_unit([])

if __name__ == '__main__':
    unittest.main()