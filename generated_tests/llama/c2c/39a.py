import unittest
from your_module import is_prime, prime_fib  # Replace with the actual module name

class TestPrimeFunctions(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(6))
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(8))
        self.assertTrue(is_prime(11))

    def test_prime_fib(self):
        self.assertEqual(prime_fib(1), 2)
        self.assertEqual(prime_fib(2), 3)
        self.assertEqual(prime_fib(3), 5)
        self.assertIsNone(prime_fib(4))  # since prime_fib_count exceeds n
        self.assertEqual(prime_fib(5), 13)

if __name__ == '__main__':
    unittest.main()