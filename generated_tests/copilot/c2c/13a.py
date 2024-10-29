import unittest
from c2c.13a import greatest_common_divisor

class TestGreatestCommonDivisor(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(greatest_common_divisor(48, 18), 6)
        self.assertEqual(greatest_common_divisor(100, 25), 25)
        self.assertEqual(greatest_common_divisor(7, 3), 1)

    def test_negative_numbers(self):
        self.assertEqual(greatest_common_divisor(-48, -18), 6)
        self.assertEqual(greatest_common_divisor(-100, -25), 25)
        self.assertEqual(greatest_common_divisor(-7, -3), 1)

    def test_mixed_sign_numbers(self):
        self.assertEqual(greatest_common_divisor(48, -18), 6)
        self.assertEqual(greatest_common_divisor(-100, 25), 25)
        self.assertEqual(greatest_common_divisor(7, -3), 1)

    def test_zero(self):
        self.assertEqual(greatest_common_divisor(0, 18), 18)
        self.assertEqual(greatest_common_divisor(48, 0), 48)
        self.assertEqual(greatest_common_divisor(0, 0), 0)

    def test_one(self):
        self.assertEqual(greatest_common_divisor(1, 18), 1)
        self.assertEqual(greatest_common_divisor(48, 1), 1)
        self.assertEqual(greatest_common_divisor(1, 1), 1)

if __name__ == '__main__':
    unittest.main()