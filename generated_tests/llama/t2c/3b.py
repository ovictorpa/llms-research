import unittest

class TestTruncateNumber(unittest.TestCase):

    def test_truncate_positive_number(self):
        self.assertAlmostEqual(truncate_number(3.5), 0.5, places=1)

    def test_truncate_negative_number(self):
        with self.assertRaises(ValueError):
            truncate_number(-1.2)

    def test_truncate_zero(self):
        self.assertEqual(truncate_number(0), 0.0)

    def test_truncate_single_integer(self):
        self.assertEqual(truncate_number(5), 0.0)

    def test_edge_case_decimal_part_equals_one(self):
        with self.assertRaises(ValueError):
            truncate_number(1.1)

if __name__ == '__main__':
    unittest.main()