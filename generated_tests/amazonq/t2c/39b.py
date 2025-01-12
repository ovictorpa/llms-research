import unittest
import math
from typing import Optional

def is_prime(p: int) -> bool:
    # Function implementation goes here
    # For testing purposes, we'll leave this empty
    pass

def prime_fib(n: int) -> Optional[int]:
    # Function implementation goes here
    # For testing purposes, we'll leave this empty
    pass

class TestPrimeFibFunctions(unittest.TestCase):
    def test_is_prime_examples(self):
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))

    def test_is_prime_edge_cases(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))

    def test_is_prime_large_numbers(self):
        self.assertTrue(is_prime(104729))  # 10,000th prime number
        self.assertFalse(is_prime(104730))

    def test_is_prime_negative_numbers(self):
        self.assertFalse(is_prime(-2))
        self.assertFalse(is_prime(-5))

    def test_prime_fib_examples(self):
        self.assertEqual(prime_fib(1), 2)
        self.assertEqual(prime_fib(2), 3)
        self.assertEqual(prime_fib(3), 5)
        self.assertEqual(prime_fib(4), 13)
        self.assertEqual(prime_fib(5), 89)

    def test_prime_fib_edge_cases(self):
        with self.assertRaises(ValueError):
            prime_fib(0)
        with self.assertRaises(ValueError):
            prime_fib(-1)

    def test_prime_fib_large_n(self):
        self.assertEqual(prime_fib(10), 433494437)

    def test_prime_fib_properties(self):
        for i in range(1, 6):
            result = prime_fib(i)
            self.assertTrue(is_prime(result), f"{result} should be prime")
            # Check if it's a Fibonacci number (using the property that a number is Fibonacci
            # if and only if one of 5n^2+4 or 5n^2-4 is a perfect square)
            n = result
            self.assertTrue(
                math.isqrt(5*n*n + 4)**2 == (5*n*n + 4) or 
                math.isqrt(5*n*n - 4)**2 == (5*n*n - 4),
                f"{result} should be a Fibonacci number"
            )

    def test_is_prime_type_error(self):
        with self.assertRaises(TypeError):
            is_prime(3.14)

    def test_prime_fib_type_error(self):
        with self.assertRaises(TypeError):
            prime_fib(3.14)

if __name__ == '__main__':
    unittest.main()
