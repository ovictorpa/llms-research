import unittest
import math

def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into an integer part 
    (largest integer smaller than given number) and decimals (leftover part always smaller than 1). 
    Return the decimal part of the number.
    """
    # Function implementation goes here
    # For testing purposes, we'll assume the function is correctly implemented

class TestTruncateNumber(unittest.TestCase):
    def test_example_case(self):
        self.assertAlmostEqual(truncate_number(3.5), 0.5)

    def test_zero(self):
        self.assertAlmostEqual(truncate_number(0.0), 0.0)

    def test_integer(self):
        self.assertAlmostEqual(truncate_number(5.0), 0.0)

    def test_small_decimal(self):
        self.assertAlmostEqual(truncate_number(0.1), 0.1)

    def test_large_decimal(self):
        self.assertAlmostEqual(truncate_number(0.9999), 0.9999)

    def test_large_number(self):
        self.assertAlmostEqual(truncate_number(1234567.89), 0.89)

    def test_very_small_decimal(self):
        self.assertAlmostEqual(truncate_number(100.000001), 0.000001)

    def test_precision(self):
        self.assertAlmostEqual(truncate_number(math.pi), math.pi - 3)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            truncate_number(-1.5)

    def test_non_float_input(self):
        with self.assertRaises(TypeError):
            truncate_number("3.5")

if __name__ == '__main__':
    unittest.main()
