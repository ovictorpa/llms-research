import unittest
from humaneval_prompts.c2c._3a import truncate_number

# File: humaneval_prompts/c2c/test_3a.py


class TestTruncateNumber(unittest.TestCase):
    def test_positive_float(self):
        self.assertAlmostEqual(truncate_number(123.456), 0.456)

    def test_negative_float(self):
        self.assertAlmostEqual(truncate_number(-123.456), -0.456)

    def test_zero(self):
        self.assertEqual(truncate_number(0), 0)

    def test_positive_integer(self):
        self.assertEqual(truncate_number(123), 0)

    def test_negative_integer(self):
        self.assertEqual(truncate_number(-123), 0)

if __name__ == '__main__':
    unittest.main()