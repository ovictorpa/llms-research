import unittest

def largest_divisor(n: int) -> int:
    # Function implementation goes here
    # For testing purposes, we'll leave this empty
    pass

class TestLargestDivisor(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(largest_divisor(15), 5)

    def test_prime_number(self):
        self.assertEqual(largest_divisor(17), 1)

    def test_even_number(self):
        self.assertEqual(largest_divisor(24), 12)

    def test_perfect_square(self):
        self.assertEqual(largest_divisor(36), 18)

    def test_large_number(self):
        self.assertEqual(largest_divisor(1000000), 500000)

    def test_power_of_two(self):
        self.assertEqual(largest_divisor(64), 32)

    def test_edge_case_one(self):
        self.assertEqual(largest_divisor(1), 1)

    def test_edge_case_two(self):
        self.assertEqual(largest_divisor(2), 1)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            largest_divisor(-10)

    def test_zero(self):
        with self.assertRaises(ValueError):
            largest_divisor(0)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            largest_divisor(15.5)

if __name__ == '__main__':
    unittest.main()
