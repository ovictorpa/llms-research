import unittest
from c2c.25a import factorize  # Adjust the import statement as needed

class TestFactorize(unittest.TestCase):

    def test_prime_number(self):
        self.assertEqual(factorize(17), [17])

    def test_composite_number(self):
        self.assertEqual(factorize(24), [2, 2, 2, 3])

    def test_square_number(self):
        self.assertEqual(factorize(25), [5, 5])

    def test_large_prime(self):
        self.assertEqual(factorize(997), [997])

    def test_product_of_primes(self):
        self.assertEqual(factorize(30), [2, 3, 5])

    def test_power_of_two(self):
        self.assertEqual(factorize(64), [2, 2, 2, 2, 2, 2])

    def test_one(self):
        self.assertEqual(factorize(1), [])

    def test_zero(self):
        with self.assertRaises(ValueError):
            factorize(0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            factorize(-10)

if __name__ == '__main__':
    unittest.main()
