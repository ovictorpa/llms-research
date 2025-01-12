import unittest

class TestGCD(unittest.TestCase):

    def test_gcd_of_two_small_numbers(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)

    def test_gcd_of_two_medium_numbers(self):
        self.assertEqual(greatest_common_divisor(25, 15), 5)

    def test_gcd_of_equal_numbers(self):
        self.assertEqual(greatest_common_divisor(10, 10), 10)

    def test_gcd_of_one_number(self):
        self.assertEqual(greatest_common_divisor(11, 2), 1)

    def test_gcd_of_negative_numbers(self):
        with self.assertRaises(ValueError):
            greatest_common_divisor(-5, -3)

    def test_gcd_with_zero(self):
        with self.assertRaises(ValueError):
            greatest_common_divisor(0, 4)

if __name__ == '__main__':
    unittest.main()