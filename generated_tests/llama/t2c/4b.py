import unittest
from typing import List

class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_mad_with_even_number_of_elements(self):
        numbers = [1.0, 2.0, 3.0, 4.0]
        self.assertAlmostEqual(mean_absolute_deviation(numbers), (sum(abs(num - sum(numbers) / len(numbers)) for num in numbers) / len(numbers)),
places=1)

    def test_mad_with_odd_number_of_elements(self):
        numbers = [1.0, 2.0, 3.0, 4.0]
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0]), (sum(abs(num - sum(numbers) / len(numbers)) for num in numbers[1:]) /
len(numbers[1:]), places=1))

    def test_mad_with_single_element(self):
        with self.assertRaises(ZeroDivisionError):
            mean_absolute_deviation([1.0])

    def test_mad_with_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            mean_absolute_deviation([])

if __name__ == '__main__':
    unittest.main()