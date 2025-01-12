import unittest

class TestGreatestCommonDivisor(unittest.TestCase):
    def test_greatest_common_divisor(self):
        # Test case 1: Positive integers with common divisor
        self.assertEqual(greatest_common_divisor(12, 18), 6)
        
        # Test case 2: Positive integers with no common divisor other than 1
        self.assertEqual(greatest_common_divisor(7, 9), 1)
        
        # Test case 3: One of the inputs is 0
        self.assertEqual(greatest_common_divisor(0, 8), 8)
        self.assertEqual(greatest_common_divisor(16, 0), 16)
        
        # Test case 4: Negative integers
        self.assertEqual(greatest_common_divisor(-12, 18), 6)

        
        # Test case 5: Large integers
        self.assertEqual(greatest_common_divisor(1234567, 8901234), 3)
        
        # Test case 6: Same integers
        self.assertEqual(greatest_common_divisor(42, 42), 42)

if __name__ == '__main__':
    unittest.main()
