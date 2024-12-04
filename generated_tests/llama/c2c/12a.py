import unittest
from your_module import longest  # Replace with the actual module name

class TestLongest(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_element(self):
        self.assertEqual(longest(["hello"]), "hello")

    def test_multiple_elements(self):
        self.assertEqual(longest(["hello", "world", "abc"]), "world")

    def test_longest_string_first(self):
        self.assertEqual(longest(["abc", "defgh", "ijklmn"]), "ijklmn")

    def test_tie(self):
        self.assertEqual(longest(["a", "b", "c", "d", "e"]), "e")


if __name__ == '__main__':
    unittest.main()