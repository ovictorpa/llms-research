import unittest

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, which is smaller than n.
    
    >>> largest_divisor(15)
    5
    """
    if n == 1:
        return 1
    for i in range(n // 2, 0, -1):
        if n % i == 0:
            return i

class TestLargestDivisor(unittest.TestCase):
    def test_example(self):
        self.assertEqual(largest_divisor(15), 5)
    
    def test_prime_number(self):
        self.assertEqual(largest_divisor(13), 1)
    
    def test_even_number(self):
        self.assertEqual(largest_divisor(10), 5)
    
    def test_odd_number(self):
        self.assertEqual(largest_divisor(9), 3)
    
    def test_one(self):
        self.assertEqual(largest_divisor(1), 1)
    
    def test_large_number(self):
        self.assertEqual(largest_divisor(100), 50)

if __name__ == '__main__':
    unittest.main()