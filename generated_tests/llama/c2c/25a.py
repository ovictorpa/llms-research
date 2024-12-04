import unittest
from your_module import factorize  # Replace with the actual module name

class TestFactorize(unittest.TestCase):
    def test_prime_number(self):
        self.assertEqual(factorize(23), [23])

    def test_composite_number(self):
        self.assertEqual(factorize(36), [2, 2, 3, 3])

    def test_square_root_factorization(self):
        self.assertEqual(factorize(24), [2, 2, 2, 3])

    def test_large_prime_number(self):
        self.assertEqual(factorize(997), [997])

    def test_perfect_square(self):
        self.assertEqual(factorize(49), [7, 7])

if __name__ == '__main__':
    unittest.main()