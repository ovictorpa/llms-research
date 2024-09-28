import unittest
from c2c.24a import largest_divisor  # Adjust the import statement as needed

class TestLargestDivisor(unittest.TestCase):

    def test_prime_number(self):
        self.assertEqual(largest_divisor(17), 1)

    def test_composite_number(self):
        self.assertEqual(largest_divisor(24), 12)

    def test_square_number(self):
        self.assertEqual(largest_divisor(25), 5)

    def test_even_number(self):
        self.assertEqual(largest_divisor(100), 50)

    def test_odd_number(self):
        self.assertEqual(largest_divisor(27), 9)

    def test_large_number(self):
        self.assertEqual(largest_divisor(1000000), 500000)

    def test_one(self):
        self.assertEqual(largest_divisor(1), 1)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            largest_divisor(-10)

    def test_zero(self):
        with self.assertRaises(ValueError):
            largest_divisor(0)

if __name__ == '__main__':
    unittest.main()
