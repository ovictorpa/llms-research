import unittest

class TestGreatestCommonDivisorFunction(unittest.TestCase):

    def test_identity(self):
        # Test that gcd of two identical numbers is the number itself
        self.assertEqual(greatest_common_divisor(12, 12), 12)

    def test_positive_numbers(self):
        # Test with positive integers
        self.assertEqual(greatest_common_divisor(24, 30), 6)

    def test_negative_numbers(self):
        # Test with negative integers (gcd remains the same when both numbers are negative)
        self.assertEqual(greatest_common_divisor(-12, -15), 3)

    def test_zero_input(self):
        # Test that gcd of zero and non-zero number is zero
        self.assertEqual(greatest_common_divisor(0, 10), 0)

    def test_non_integer_inputs(self):
        # Test that type error is raised when inputs are not integers
        with self.assertRaises(TypeError):
            greatest_common_divisor("a", 10)

if __name__ == '__main__':
    unittest.main()