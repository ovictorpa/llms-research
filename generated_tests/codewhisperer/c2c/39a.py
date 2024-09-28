import unittest
from c2c.39a import prime_fib  # Adjust the import statement as needed

class TestPrimeFib(unittest.TestCase):

    def test_first_prime_fib(self):
        self.assertEqual(prime_fib(1), 2)

    def test_second_prime_fib(self):
        self.assertEqual(prime_fib(2), 3)

    def test_third_prime_fib(self):
        self.assertEqual(prime_fib(3), 5)

    def test_fourth_prime_fib(self):
        self.assertEqual(prime_fib(4), 13)

    def test_fifth_prime_fib(self):
        self.assertEqual(prime_fib(5), 89)

    def test_sixth_prime_fib(self):
        self.assertEqual(prime_fib(6), 233)

    def test_seventh_prime_fib(self):
        self.assertEqual(prime_fib(7), 1597)

    def test_invalid_input_zero(self):
        with self.assertRaises(ValueError):
            prime_fib(0)

    def test_invalid_input_negative(self):
        with self.assertRaises(ValueError):
            prime_fib(-1)

    def test_large_input(self):
        # This test might take some time to run
        self.assertEqual(prime_fib(10), 514229)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            prime_fib("1")

if __name__ == '__main__':
    unittest.main()
