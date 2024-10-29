import unittest
from c2c._22a import filter_integers

class TestFilterIntegers(unittest.TestCase):

    def test_all_integers(self):
        self.assertEqual(filter_integers([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_mixed_types(self):
        self.assertEqual(filter_integers([1, 'a', 2.5, 3, 'b']), [1, 3])

    def test_no_integers(self):
        self.assertEqual(filter_integers(['a', 'b', 2.5, 3.5]), [])

    def test_empty_list(self):
        self.assertEqual(filter_integers([]), [])

    def test_negative_integers(self):
        self.assertEqual(filter_integers([-1, -2, 'a', 3]), [-1, -2, 3])

    def test_single_integer(self):
        self.assertEqual(filter_integers([42]), [42])

    def test_single_non_integer(self):
        self.assertEqual(filter_integers(['a']), [])

if __name__ == '__main__':
    unittest.main()