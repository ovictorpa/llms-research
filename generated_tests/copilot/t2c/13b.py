import unittest

def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor (GCD) of two integers a and b using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return abs(a)

class TestGreatestCommonDivisor(unittest.TestCase):
    def test_example_cases(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)
    
    def test_zero_cases(self):
        self.assertEqual(greatest_common_divisor(0, 5), 5)
        self.assertEqual(greatest_common_divisor(5, 0), 5)
        self.assertEqual(greatest_common_divisor(0, 0), 0)
    
    def test_negative_numbers(self):
        self.assertEqual(greatest_common_divisor(-25, 15), 5)
        self.assertEqual(greatest_common_divisor(25, -15), 5)
        self.assertEqual(greatest_common_divisor(-25, -15), 5)
    
    def test_same_numbers(self):
        self.assertEqual(greatest_common_divisor(7, 7), 7)
        self.assertEqual(greatest_common_divisor(-7, -7), 7)

if __name__ == '__main__':
    unittest.main()