import unittest
from humaneval_prompts.c2c._4a import mean_absolute_deviation

# c2c/test_4a.py

class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_positive_numbers(self):
        numbers = [1, 2, 3, 4, 5]
        result = mean_absolute_deviation(numbers)
        expected = 1.2
        self.assertAlmostEqual(result, expected, places=5)

    def test_negative_numbers(self):
        numbers = [-1, -2, -3, -4, -5]
        result = mean_absolute_deviation(numbers)
        expected = 1.2
        self.assertAlmostEqual(result, expected, places=5)

    def test_mixed_numbers(self):
        numbers = [-1, 0, 1]
        result = mean_absolute_deviation(numbers)
        expected = 0.6666666667
        self.assertAlmostEqual(result, expected, places=5)

    def test_single_number(self):
        numbers = [5]
        result = mean_absolute_deviation(numbers)
        expected = 0.0
        self.assertAlmostEqual(result, expected, places=5)

    def test_empty_list(self):
        numbers = []
        with self.assertRaises(ZeroDivisionError):
            mean_absolute_deviation(numbers)

if __name__ == '__main__':
    unittest.main()