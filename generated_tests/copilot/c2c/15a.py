import unittest
from c2c.15a import string_sequence

class TestStringSequence(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(string_sequence(0), "0")

    def test_positive_number(self):
        self.assertEqual(string_sequence(5), "0 1 2 3 4 5")

    def test_single_digit(self):
        self.assertEqual(string_sequence(1), "0 1")

    def test_large_number(self):
        self.assertEqual(string_sequence(10), "0 1 2 3 4 5 6 7 8 9 10")

    def test_negative_number(self):
        self.assertEqual(string_sequence(-1), "")

if __name__ == '__main__':
    unittest.main()