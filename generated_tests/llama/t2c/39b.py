import unittest
from your_module import is_prime, prime_fib 

class TestIsPrime(unittest.TestCase):

    def test_is_prime_1(self):
        self.assertTrue(is_prime(2))

    def test_is_prime_2(self):
        self.assertFalse(is_prime(4))

    def test_is_prime_3(self):
        self.assertTrue(is_prime(5))

if __name__ == '__main__':
    unittest.main()

class TestPrimeFib(unittest.TestCase):

    def test_prime_fib_1(self):
        self.assertEqual(prime_fib(1), 2)

    def test_prime_fib_2(self):
        self.assertEqual(prime_fib(2), 3)

    def test_prime_fib_3(self):
        self.assertEqual(prime_fib(3), 5)

    def test_prime_fib_4(self):
        self.assertEqual(prime_fib(4), 13)

    def test_prime_fib_5(self):
        self.assertEqual(prime_fib(5), 89)

if __name__ == '__main__':
    unittest.main()