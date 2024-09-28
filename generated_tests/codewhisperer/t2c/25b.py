import unittest
from typing import List
import math

def factorize(n: int) -> List[int]:
    # Function implementation goes here
    # For testing purposes, we'll leave this empty
    pass

class TestFactorize(unittest.TestCase):
    def test_example_case_1(self):
        self.assertEqual(factorize(8), [2, 2, 2])

    def test_example_case_2(self):
        self.assertEqual(factorize(25), [5, 5])

    def test_example_case_3(self):
        self.assertEqual(factorize(70), [2, 5, 7])

    def test_prime_number(self):
        self.assertEqual(factorize(17), [17])

    def test_large_number(self):
        self.assertEqual(factorize(3628800), [2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 5, 5, 7])

    def test_power_of_two(self):
        self.assertEqual(factorize(64), [2, 2, 2, 2, 2, 2])

    def test_product_of_primes(self):
        self.assertEqual(factorize(2 * 3 * 5 * 7 * 11 * 13), [2, 3, 5, 7, 11, 13])

    def test_one(self):
        self.assertEqual(factorize(1), [])

    def test_zero(self):
        with self.assertRaises(ValueError):
            factorize(0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            factorize(-10)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            factorize(15.5)

    def test_product_of_factors(self):
            factors = factorize(n)
            self.assertEqual(math.prod(factors), n)

    def test_factors_in_ascending_order(self):
            factors = factorize(n)
            self.assertEqual(factors, sorted(factors))

if __name__ == '__main__':
    unittest.main()
