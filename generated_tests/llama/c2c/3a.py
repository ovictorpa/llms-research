import unittest

def truncate_number(number: float) -> float:
    return number % 1.0

class TestTruncateNumberFunction(unittest.TestCase):

    def test_whole_numbers(self):
        # Test with whole numbers (no decimal part)
        self.assertEqual(truncate_number(10), 10)
        self.assertEqual(truncate_number(20), 20)

    def test_decimal_numbers(self):
        # Test with decimal numbers
        self.assertAlmostEqual(truncate_number(3.14), 0)
        self.assertAlmostEqual(truncate_number(2.71), 2)
        self.assertAlmostEqual(truncate_number(-1.99), -1)

    def test_edge_cases(self):
        # Test edge cases (e.g., negative numbers, zero)
        self.assertEqual(truncate_number(-10), -10)
        self.assertEqual(truncate_number(0), 0)

if __name__ == '__main__':
    unittest.main()