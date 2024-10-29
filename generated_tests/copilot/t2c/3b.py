import unittest

def truncate_number(number: float) -> float:
    return number - int(number)

class TestTruncateNumber(unittest.TestCase):
    def test_basic_functionality(self):
        self.assertEqual(truncate_number(3.5), 0.5)
        self.assertEqual(truncate_number(10.75), 0.75)
        self.assertEqual(truncate_number(0.99), 0.99)

    def test_whole_numbers(self):
        self.assertEqual(truncate_number(4.0), 0.0)
        self.assertEqual(truncate_number(100.0), 0.0)

    def test_small_numbers(self):
        self.assertEqual(truncate_number(0.001), 0.001)
        self.assertEqual(truncate_number(0.0001), 0.0001)

    def test_large_numbers(self):
        self.assertEqual(truncate_number(123456.789), 0.789)
        self.assertEqual(truncate_number(987654321.123), 0.123)

if __name__ == '__main__':
    unittest.main()