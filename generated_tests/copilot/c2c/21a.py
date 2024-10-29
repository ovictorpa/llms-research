import unittest
from c2c import rescale_to_unit

class TestRescaleToUnit(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(rescale_to_unit([1, 2, 3, 4, 5]), [0.0, 0.25, 0.5, 0.75, 1.0])

    def test_negative_numbers(self):
        self.assertEqual(rescale_to_unit([-5, -4, -3, -2, -1]), [0.0, 0.25, 0.5, 0.75, 1.0])

    def test_mixed_numbers(self):
        self.assertEqual(rescale_to_unit([-1, 0, 1]), [0.0, 0.5, 1.0])

    def test_single_number(self):
        self.assertEqual(rescale_to_unit([42]), [0.0])

    def test_empty_list(self):
        self.assertEqual(rescale_to_unit([]), [])

    def test_identical_numbers(self):
        self.assertEqual(rescale_to_unit([3, 3, 3]), [0.0, 0.0, 0.0])

if __name__ == '__main__':
    unittest.main()