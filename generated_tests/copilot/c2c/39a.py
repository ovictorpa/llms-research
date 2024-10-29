import unittest
from c2c._39a import prime_fib

class TestPrimeFib(unittest.TestCase):

    def test_prime_fib_first_prime(self):
        self.assertEqual(prime_fib(1), 2)

    def test_prime_fib_second_prime(self):
        self.assertEqual(prime_fib(2), 3)

    def test_prime_fib_third_prime(self):
        self.assertEqual(prime_fib(3), 5)

    def test_prime_fib_fourth_prime(self):
        self.assertEqual(prime_fib(4), 13)

    def test_prime_fib_fifth_prime(self):
        self.assertEqual(prime_fib(5), 89)

    def test_prime_fib_sixth_prime(self):
        self.assertEqual(prime_fib(6), 233)

    def test_prime_fib_seventh_prime(self):
        self.assertEqual(prime_fib(7), 1597)

    def test_prime_fib_eighth_prime(self):
        self.assertEqual(prime_fib(8), 28657)

    def test_prime_fib_ninth_prime(self):
        self.assertEqual(prime_fib(9), 514229)

    def test_prime_fib_tenth_prime(self):
        self.assertEqual(prime_fib(10), 433494437)

if __name__ == '__main__':
    unittest.main()