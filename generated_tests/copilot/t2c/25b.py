import unittest
from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return a list of prime factors of the given integer in ascending order.
    Each factor is listed according to how many times it appears in the factorization.
    The input number should be equal to the product of all factors.
    
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    # Check for number of 2s in n
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    # n must be odd at this point so a skip of 2 (i.e., i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        # while i divides n, append i and divide n
        while n % i == 0:
            factors.append(i)
            n = n // i
    # Condition if n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    return factors

class TestFactorize(unittest.TestCase):
    def test_example_8(self):
        self.assertEqual(factorize(8), [2, 2, 2])
    
    def test_example_25(self):
        self.assertEqual(factorize(25), [5, 5])
    
    def test_example_70(self):
        self.assertEqual(factorize(70), [2, 5, 7])
    
    def test_prime_number(self):
        self.assertEqual(factorize(13), [13])
    
    def test_large_number(self):
        self.assertEqual(factorize(100), [2, 2, 5, 5])
    
    def test_one(self):
        self.assertEqual(factorize(1), [])

if __name__ == '__main__':
    unittest.main()