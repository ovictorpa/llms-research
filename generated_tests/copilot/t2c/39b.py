import unittest
import math
from typing import Optional

def is_prime(p: int) -> bool:
    """
    Check if a number is prime.
    
    >>> is_prime(2)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    """
    if p <= 1:
        return False
    if p <= 3:
        return True
    if p % 2 == 0 or p % 3 == 0:
        return False
    i = 5
    while i * i <= p:
        if p % i == 0 or p % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_fib(n: int) -> Optional[int]:
    """
    Returns the n-th number that is both a Fibonacci number and a prime.
    
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    def fibonacci():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
    
    count = 0
    for f in fibonacci():
        if is_prime(f):
            count += 1
            if count == n:
                return f

class TestPrimeFunctions(unittest.TestCase):
    def test_is_prime_example_1(self):
        self.assertTrue(is_prime(2))
    
    def test_is_prime_example_2(self):
        self.assertFalse(is_prime(4))
    
    def test_is_prime_example_3(self):
        self.assertTrue(is_prime(5))
    
    def test_is_prime_negative(self):
        self.assertFalse(is_prime(-5))
    
    def test_is_prime_zero(self):
        self.assertFalse(is_prime(0))
    
    def test_is_prime_one(self):
        self.assertFalse(is_prime(1))
    
    def test_prime_fib_example_1(self):
        self.assertEqual(prime_fib(1), 2)
    
    def test_prime_fib_example_2(self):
        self.assertEqual(prime_fib(2), 3)
    
    def test_prime_fib_example_3(self):
        self.assertEqual(prime_fib(3), 5)
    
    def test_prime_fib_example_4(self):
        self.assertEqual(prime_fib(4), 13)
    
    def test_prime_fib_example_5(self):
        self.assertEqual(prime_fib(5), 89)
    
    def test_prime_fib_large(self):
        self.assertEqual(prime_fib(6), 233)

if __name__ == '__main__':
    unittest.main()