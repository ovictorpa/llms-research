import unittest
from c2c._25a import factorize

class TestFactorize(unittest.TestCase):

    def test_prime_number(self):
        self.assertEqual(factorize(13), [13], "Should be [13]")

    def test_composite_number(self):
        self.assertEqual(factorize(28), [2, 2, 7], "Should be [2, 2, 7]")

    def test_one(self):
        self.assertEqual(factorize(1), [], "Should be []")

    def test_large_prime_number(self):
        self.assertEqual(factorize(97), [97], "Should be [97]")

    def test_large_composite_number(self):
        self.assertEqual(factorize(100), [2, 2, 5, 5], "Should be [2, 2, 5, 5]")

    def test_square_number(self):
        self.assertEqual(factorize(49), [7, 7], "Should be [7, 7]")

    def test_power_of_two(self):
        self.assertEqual(factorize(16), [2, 2, 2, 2], "Should be [2, 2, 2, 2]")

if __name__ == '__main__':
    unittest.main()