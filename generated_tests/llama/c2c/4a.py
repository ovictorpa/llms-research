import unittest

class TestMeanAbsoluteDeviationFunction(unittest.TestCase):

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            mean_absolute_deviation([])

    def test_single_element_list(self):
        # Test with a list containing only one element
        self.assertAlmostEqual(mean_absolute_deviation([10]), 0)

    def test_consistent_numbers(self):
        # Test with numbers that are consistently above the mean
        self.assertLessEqual(mean_absolute_deviation([5, 6, 7, 8, 9]), 1)

    def test_inconsistent_numbers(self):
        # Test with numbers that have different values around the mean
        self.assertLessEqual(mean_absolute_deviation([2.4, 4.5, 3.1, 5.0, 1.6]), 1)

    def test_symmetricallydistributed_numbers(self):
        # Test with symmetrically distributed numbers (e.g., -10 and +10)
        self.assertAlmostEqual(mean_absolute_deviation([-5, -3, -7, -9, -1]), 2)

if __name__ == '__main__':
    unittest.main()