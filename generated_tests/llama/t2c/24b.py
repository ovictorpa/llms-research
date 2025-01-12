import unittest

class TestLargestDivisor(unittest.TestCase):

    def test_largest_divisor_even_number(self):
        self.assertEqual(largest_divisor(15), 5)

    def test_largest_divisor_odd_number(self):
        self.assertEqual(largest_divisor(17), 1)

    def test_largest_divisor_single_digit(self):
        self.assertEqual(largest_divisor(3), 1)

    def test_largest_divisor_one(self):
        self.assertEqual(largest_divisor(1), 1)

    def test_largest_divisor_zero(self):
        with self.assertRaises(ValueError):
            largest_divisor(0)  # Replacing the input with zero to raise an error

if __name__ == '__main__':
    unittest.main()