import unittest

def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor (GCD) of two integers a and b using the Euclidean algorithm.
    
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Function implementation goes here
    # For testing purposes, we'll assume the function is correctly implemented

class TestGreatestCommonDivisor(unittest.TestCase):
    def test_example_cases(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)

    def test_zero_inputs(self):
        self.assertEqual(greatest_common_divisor(0, 0), 0)
        self.assertEqual(greatest_common_divisor(0, 5), 5)
        self.assertEqual(greatest_common_divisor(5, 0), 5)

    def test_negative_inputs(self):
        self.assertEqual(greatest_common_divisor(-3, 5), 1)
        self.assertEqual(greatest_common_divisor(3, -5), 1)
        self.assertEqual(greatest_common_divisor(-3, -5), 1)

    def test_large_inputs(self):
        self.assertEqual(greatest_common_divisor(1000000, 2000000), 1000000)
        self.assertEqual(greatest_common_divisor(2000000, 1000000), 1000000)

    def test_coprime_inputs(self):
        self.assertEqual(greatest_common_divisor(7, 11), 1)
        self.assertEqual(greatest_common_divisor(13, 17), 1)

    def test_same_inputs(self):
        self.assertEqual(greatest_common_divisor(10, 10), 10)
        self.as
    def test_one_input(self):
        self.assertEqual(greatest_common_divisor(1, 10), 1)
        self.assertEqual(greatest_common_divisor(10, 1), 1)

    def test_non_integer_inputs(self):
        with self.assertRaises(TypeError):
            greatest_common_divisor(3.5, 5)
        with self.assertRaises(TypeError):
            greatest_common_divisor(3, 5.5)

    def test_non_numeric_inputs(self):
        with self.assertRaises(TypeError):
            greatest_common_divisor('a', 5)
        with self.assertRaises(TypeError):
            greatest_common_divisor(3, 'b')

if __name__ == '__main__':
    unittest.main()
