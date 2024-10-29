import unittest
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    if not numbers:
        return 0.0
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_basic_functionality(self):
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)
        self.assertAlmostEqual(mean_absolute_deviation([10.0, 20.0, 30.0, 40.0]), 10.0)

    def test_empty_list(self):
        self.assertAlmostEqual(mean_absolute_deviation([]), 0.0)

    def test_identical_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([5.0, 5.0, 5.0, 5.0]), 0.0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0]), 1.0)
        self.assertAlmostEqual(mean_absolute_deviation([-10.0, -20.0, -30.0, -40.0]), 10.0)

if __name__ == '__main__':
    unittest.main()