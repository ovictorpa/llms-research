import unittest

class TestLargestDivisorFunction(unittest.TestCase):

    def test_perfect_square(self):
        # Test with a perfect square number
        self.assertEqual(largest_divisor(25), 5)

    def test_perfect_cube(self):
        # Test with a perfect cube number
        self.assertEqual(largest_divisor(27), 3)

    def test_prime_number(self):
        # Test with a prime number
        self.assertEqual(largest_divisor(23), 1)

    def test_composite_number(self):
        # Test with a composite number
        self.assertEqual(largest_divisor(12), 6)

    def test_edge_case(self):
        # Test with the edge case of 1
        self.assertEqual(largest_divisor(1), 1)

    def test_input_not_an_integer(self):
        # Test with non-integer input
        with self.assertRaises(TypeError):
            largest_divisor(3.5)

    def test_negative_number(self):
        # Test with negative number
        with self.assertRaises(ValueError):  # assuming ValueError is raised for negative numbers
            largest_divisor(-12)

if __name__ == '__main__':
    unittest.main()