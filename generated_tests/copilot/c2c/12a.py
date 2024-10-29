import unittest
from c2c import 12a

class TestLongestFunction(unittest.TestCase):

    def test_longest_with_multiple_strings(self):
        self.assertEqual(longest(["apple", "banana", "cherry"]), "banana")

    def test_longest_with_single_string(self):
        self.assertEqual(longest(["apple"]), "apple")

    def test_longest_with_empty_list(self):
        self.assertIsNone(longest([]))

    def test_longest_with_strings_of_same_length(self):
        self.assertEqual(longest(["dog", "cat", "bat"]), "dog")

    def test_longest_with_mixed_length_strings(self):
        self.assertEqual(longest(["a", "ab", "abc", "abcd"]), "abcd")

    def test_longest_with_none(self):
        self.assertIsNone(longest(None))

if __name__ == '__main__':
    unittest.main()