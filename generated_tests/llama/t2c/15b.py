import unittest

class TestStringSequence(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(string_sequence(0), '0')

    def test_single_element_sequence(self):
        self.assertEqual(string_sequence(1), '0')

    def test_multiple_element_sequence(self):
        self.assertEqual(string_sequence(5), '0 1 2 3 4 5')

    def test_large_number(self):
        self.assertEqual(string_sequence(100), '0 1 2 ... 99 100')

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            string_sequence(-1)

if __name__ == '__main__':
    unittest.main()