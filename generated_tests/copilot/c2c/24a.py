import unittest
from c2c._24a import largest_divisor

class TestLargestDivisor(unittest.TestCase):

    def test_largest_divisor_of_10(self):
        self.assertEqual(largest_divisor(10), 5)

    def test_largest_divisor_of_15(self):
        self.assertEqual(largest_divisor(15), 5)

    def test_largest_divisor_of_17(self):
        self.assertEqual(largest_divisor(17), 1)

    def test_largest_divisor_of_1(self):
        self.assertEqual(largest_divisor(1), 1)

    def test_largest_divisor_of_100(self):
        self.assertEqual(largest_divisor(100), 50)

    def test_largest_divisor_of_49(self):
        self.assertEqual(largest_divisor(49), 7)

if __name__ == '__main__':
    unittest.main()